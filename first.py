from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='DAG-1',
    start_date=datetime(2021, 6, 1),
    default_args=default_args,
    catchup=False,
    schedule_interval='@once'
) as dag:
    t1 = DummyOperator(
        task_id='DAG-1-t1',
        dag=dag
    )
    
    t2 = DummyOperator(
        task_id='DAG-1-t2',
        dag=dag
    )

    t1 >> t2
