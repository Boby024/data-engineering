from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta, timezone
from scripts import apis, databases



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(timezone.utc) + timedelta(minutes=5),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


with DAG("etl_with_dbt", schedule_interval="@daily", default_args=default_args) as dag:
    # Extract from multiple sources

    extract_e1 = PythonOperator(
        task_id="extract_api_test",
        python_callable=apis.Test().save()
    )

    # extract_e2 = PythonOperator(
    #     task_id="extract_database_postgresql",
    #     python_callable=databases.PostgresSQL(uri="", table_name="").save()
    # )

    # # Transform with DBT
    # dbt_run = BashOperator(
    #     task_id="transformation_dbt_run",
    #     bash_command="xxxx"
    # )

    # extract_e1 >> extract_e2 >> dbt_run
    extract_e1
