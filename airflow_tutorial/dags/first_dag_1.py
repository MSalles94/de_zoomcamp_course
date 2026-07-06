from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'matheus',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
    }

with DAG(
    dag_id='first_dag_v1',
    default_args=default_args,
    description='This is the first airflow dag'
    ,start_date=datetime(2026,7,6,11,45)
    ,schedule='@daily'
    ,catchup=False

    
) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

  

    task1
  