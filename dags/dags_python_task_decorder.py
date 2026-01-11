from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="custom_python_task_dag",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    @task(task_id="print_the_context")
    def print_context(some_input):
        print(some_input)
    
    python_task_1 = print_context("Hello from Airflow PythonOperator!")    