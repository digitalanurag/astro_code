from datetime import datetime
 
from airflow import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
 
 
with DAG(
    dag_id="trigger_dbt_cloud_job",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["dbt_cloud"],
) as dag:
 
    run_dbt_job = DbtCloudRunJobOperator(
        task_id="run_dbt_cloud_job",
        dbt_cloud_conn_id="astro_dbt_connn",
        account_id=70506183155690,
        job_id=70506183136984,
        steps_override=[
            "dbt run --select my_second_dbt_model"
        ],
        wait_for_termination=True,
        check_interval=10,
    )
 
