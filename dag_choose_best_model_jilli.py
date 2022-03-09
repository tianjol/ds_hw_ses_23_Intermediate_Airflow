from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator


def _choose_best_model():
    accuracy=6
    if accuracy>5:
        return 'accurate'
    else :
        return  'inaccurate'
      
    
with DAG(
    dag_id='dag_choose_best_model_jilli.py',
    schedule_interval='*/5 * * * *',
    start_date=datetime(2022,3,7),
    catchup=False
) as dag:
    start = DummyOperator(
        task_id='start'
    )
    choose_best_model = BranchPythonOperator(
        task_id='choose_best_model',
        python_callable=_choose_best_model
    )
    accurate = DummyOperator(
        task_id='accurate'
    )
    inaccurate = DummyOperator(
        task_id='inaccurate'
    )
    start >> choose_best_model >> [accurate, inaccurate]