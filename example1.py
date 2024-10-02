import datetime
import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

import time

def long_running_task():
    time.sleep(1000000000)
    raise Exception("This task is designed to fail.")

with DAG(
    dag_id="Example1",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    dagrun_timeout=datetime.timedelta(minutes=60),
    catchup=False,
    on_success_callback=None,
    tags=["everton-arakaki-test"],
) as dag:

    tasks = [PythonOperator(
        task_id=f"task{i}",
        python_callable=long_running_task
    ) for i in range(18)]
    end = EmptyOperator(task_id="end")

    [tasks] >> end
