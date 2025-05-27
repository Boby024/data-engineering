# data-engineering

<h2>Project 1: ETL (with Airflow and DBT)</h2>
<span>
Build a pipeline that extracts data from multiple sources (e.g., API, CSV, or database), transforms them with dbt (e.g., cleaning, enrichment), and loads it into a data warehouse (e.g., PostgreSQL, BigQuery, etc.).
</span><br>
<span>Pipeline Structure</span>
<ul>
    <li>Extract: Use Airflow to pull raw data from a source (e.g., API or database) and load it into a raw/staging schema in your data warehouse.</li>
    <li>Transform: Use dbt to run transformations on staged data into analytics-ready models.</li>
    <li>Load: dbt transformations typically are the load into the final tables</li>
</ul>

<h2>Project 2: Business Intelligence</h2>