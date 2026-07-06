from datetime import datetime,timedelta
from airflow import DAG
#from airflow.operators.bash import BashOperator,PythonOperator
from airflow.operators.python import  PythonOperator

def get_first_name(ti):
    ti.xcom_push(key='first_name',value='Matheus') 

def get_last_name(ti):
    ti.xcom_push(key='last_name',value='Salles')

def get_age(ti):
    ti.xcom_push(key='age',value=32)

def test_python_task(ti):
    first_name=ti.xcom_pull(task_ids='t_FirstName',key='first_name')
    last_name=ti.xcom_pull(task_ids='t_LastName',key='last_name')
    age=ti.xcom_pull(task_ids='t_Age',key='age')

    print(f"""Helo world, this is the mensage: 
          My name is {first_name} {last_name} and I'm {age} years old.""" )


default_args={
    'owner':'matheus',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
    }

with DAG(
    dag_id='first_dag_v4',
    default_args=default_args,
    description='This is the first airflow dag'
    ,start_date=datetime(2026,7,6,11,45)
    ,schedule='@daily'
    ,catchup=False

    
) as dag:
    task1=PythonOperator(
        task_id='t_FirstName'
        ,python_callable=get_first_name
    )

    task2=PythonOperator(
        task_id='t_LastName'
        ,python_callable=get_last_name
    )
    task3=PythonOperator(
        task_id='t_Age'
        ,python_callable=get_age
    )

    task4=PythonOperator(
        task_id='mensage_task',
        python_callable=test_python_task
    )
    
 
    [task1, task2, task3] >> task4

     
   
  