from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago 
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
        dag_id='test_airflow_run_job',
        start_date=days_ago(0),
        schedule_interval="@daily",
        tags=["Test"]
) as dag:
    
    # task1 = 
    # BashOperator(
    #     task_id="DBT",
    #     bash_command='dbt run --models /app/models/example.*sql'
    # )
    task1 = DockerOperator(
        task_id='run_dbt',
        image='test_dbt:1.0.1',
        api_version='auto',
        network_mode="bridge",
        #docker_url="unix://var/run/docker.sock",
        # volumes=["test_dockop_data_path:/home/airflow/data"],
        docker_url='tcp://docker-proxy:2375',
        command='dbt run --models /app/models/example.*sql',
    )


    task1
