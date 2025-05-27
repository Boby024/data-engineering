# data-engineering

<div>
<h2>Project 1: ETL (with Airflow and DBT)</h2>
<span>
Build a pipeline that extracts data from multiple sources (e.g., API, CSV, or database), transforms them with dbt (e.g., cleaning, enrichment), and loads it into a data warehouse (e.g., PostgreSQL, Microsoft SQL Server, Azure Data Lake, MongoDB etc.).
</span><br>
<span>Pipeline Structure</span>
<ul>
    <li>Extract: Use Airflow to pull raw data from a source (e.g., API or database) and load it into a raw/staging schema in your data warehouse.</li>
    <li>Transform: Use dbt to run transformations on staged data into analytics-ready models.</li>
    <li>Load: dbt transformations typically are the load into the final tables</li>
</ul>

<div>
    <span>Steps for Airflow Configuration:</span>
    <ul>
        <li>Move into folder "etl"</li>
        <li>Make sure you already hast Database URL where to save airflow details (such as users, roles, dags)</li>
        <li>Create a .env file where AIRFLOW__DATABASE__SQL_ALCHEMY_CONN and USER detail are saved</li>
        <li>Make the file "init_airflow.sh" (to init and create new user havinf access to airflow web UI) executable 
            by running the command: chmod +x init_airflow.sh
        </li>
        <li>To init the airflow database, run: ./init_airflow.sh 0 </li>
        <li>To create a new user for airflow web UI, run: ./init_airflow.sh 1 and to list all users with: airflow users list </li>
    </ul>
</div>

<div>
    <span>Run Airflow:</span>
    <ul>
        <li>Run Airflow Web UI: airflow webserver or airflow webserver --port 8080</li>
    </ul>
</div>
</div>

<div>
    <h2>Project 2: Business Intelligence</h2>
</div>