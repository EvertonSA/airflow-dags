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
    start_date=pendulum.datetime(2024, 10, 1, tz="UTC"),
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

    tasks >> end


# Traceback (most recent call last):
#   File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskmixin.py", line 271, in set_upstream
#     self._set_relatives(task_or_task_list, upstream=True, edge_modifier=edge_modifier)
#   File "/home/airflow/.local/lib/python3.12/site-packages/airflow/models/taskmixin.py", line 215, in _set_relatives
#     task_object.update_relative(self, not upstream, edge_modifier=edge_modifier)
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'list' object has no attribute 'update_relative'