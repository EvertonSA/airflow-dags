import datetime
import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="Example1",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    dagrun_timeout=datetime.timedelta(minutes=60),
    catchup=False,
    on_success_callback=None,
    tags=["everton-arakaki-test"],
) as dag:

    start = EmptyOperator(task_id="start")
    task1 = EmptyOperator(task_id="task1")
    end = EmptyOperator(task_id="end")

start >> task1 >> end
