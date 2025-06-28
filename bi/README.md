  <h1>🚀 Metabase Docker Compose Setup</h1>

  <p>This project runs <strong>Metabase</strong> with Docker Compose, using a <code>.env</code> file for configuration.</p>
  <p>It supports custom JDBC drivers (e.g. Oracle, Vertica) and persistent storage.</p>

  <h2>📂 Folder Structure</h2>
  <pre>
project-root/
├── docker-compose.yml
├── .env
├── metabase-data-volumes/   # Stores Metabase metadata
└── plugins/                 # Store JDBC drivers here (Oracle, Vertica, etc.)
  </pre>

  <h2>⚙️ Environment Variables</h2>

  <p>Define these in your <code>.env</code> file:</p>
  <pre>
MB_DB_TYPE=postgres
MB_DB_DBNAME=metabase_db
MB_DB_PORT=5432
MB_DB_USER=metabase_user
MB_DB_PASS=metabase_pass
MB_DB_HOST=db.example.com

MB_PORT=3000
  </pre>

  <p>These configure the <strong>Metabase internal database</strong> — where Metabase stores dashboards, configs, etc. They <strong>do not configure your analytics data sources</strong>.</p>

  <h2>🗂️ Volumes</h2>

  <p>These folders must exist and be writable:</p>
  <ul>
    <li><code>metabase-data-volumes</code>: Metabase internal metadata.</li>
    <li><code>plugins</code>: Third-party JDBC drivers.</li>
  </ul>

  <pre>
mkdir -p metabase-data-volumes
mkdir -p plugins
chmod -R 777 plugins
  </pre>

  <h2>🔌 Adding Oracle or Vertica JDBC Drivers</h2>
  <p>Due to licensing restrictions, Metabase cannot ship Oracle or Vertica JDBC drivers. Download them manually and place them in <code>plugins/</code>.</p>
  <pre>
plugins/
 ├── ojdbc11.jar                  # Oracle JDBC driver
 ├── vertica-jdbc-24.2.0-1.jar    # Vertica JDBC driver
  </pre>

  <h2>⚙️ docker-compose.yml</h2>

  <p>
    ✅ <strong>Note:</strong><br>
    - <code>hostname: metabase</code> ensures the Quartz scheduler works properly.<br>
    - <strong>Do not use</strong> <code>network_mode: host</code> with <code>hostname</code> — this breaks DNS resolution.
  </p>

  <p>
  The <code>user: "2000:2000"</code> line in the Docker Compose file tells Docker to run the Metabase container as a specific non-root user with user ID 2000 and group ID 2000. This improves security by preventing the container from running as the root user and ensures that any files created in mounted volumes (like <code>metabase-data-volumes</code> or <code>plugins</code>) are owned by this user ID on the host system. It helps avoid permission issues and follows best practices for running containers securely.
  </p>

  <h2>⚡ Starting Metabase</h2>
  <pre>
docker-compose up -d
  </pre>
  <p>Open <a href="http://localhost:3000" target="_blank">http://localhost:3000</a></p>

  <h2>📊 Connecting to Your Data Warehouse</h2>

  <p>By default, Metabase does not connect to your analytics databases automatically. Add them in the UI:</p>
  <ol>
    <li>Open Metabase at <a href="http://localhost:3000" target="_blank">http://localhost:3000</a></li>
    <li>Go to <strong>Admin → Databases → Add Database</strong></li>
    <li>Fill in your PostgreSQL, Oracle, Vertica, etc.</li>
  </ol>

  <!-- <h3>✅ Optional: Automate It</h3>

  <p>You can add your data warehouse automatically using the Metabase API:</p>
  <pre>
curl -X POST http://localhost:3000/api/database \
  -H "Content-Type: application/json" \
  -H "X-Metabase-Session: YOUR_SESSION_TOKEN" \
  -d '{
    "name": "My Warehouse",
    "engine": "postgres",
    "details": {
      "host": "warehouse-host",
      "port": 5432,
      "dbname": "warehouse_db",
      "user": "warehouse_user",
      "password": "warehouse_password"
    }
  }' -->
  
  </pre>

  <h2>✅ Troubleshooting</h2>
  <ul>
    <li><strong>Couldn’t generate instance Id!</strong><br>
      ➜ Do not use <code>network_mode: host</code> with <code>hostname</code>. Remove host mode or hostname.
    </li>
    <li><strong>Cannot initialize plugin</strong> (Oracle, Vertica)<br>
      ➜ Make sure your <code>.jar</code> files are in <code>plugins/</code> and the folder has correct permissions.
    </li>
    <li><strong>Falling back to temporary plugins directory</strong><br>
      ➜ Fix folder permissions:
      <pre>chmod -R 777 plugins</pre>
    </li>
  </ul>

  <h2>✅ Stopping Metabase</h2>
  <pre>
docker-compose down
  </pre>

  <h2>✅ Good to Know</h2>
  <ul>
    <li><a href="https://www.metabase.com/docs/latest/" target="_blank">Official Metabase Docs</a></li>
    <li><a href="https://www.metabase.com/docs/latest/administration-guide/databases/oracle.html" target="_blank">Oracle Plugin Docs</a></li>
    <li><a href="https://www.metabase.com/docs/latest/administration-guide/databases/vertica.html" target="_blank">Vertica Plugin Docs</a></li>
  </ul>

  <p>Happy BI! 🎉</p>
