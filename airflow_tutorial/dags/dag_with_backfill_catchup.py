from datetime import datetime,timedelta

from airflow.decorators import dag,task


default_args={
    'owner':'Matheus',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

@dag(
    dag_id="backfill_and_catchup",
    default_args=default_args,
    start_date=datetime(2026,7,1,1),
    schedule='@daily',
    catchup=False
)
def task_definition():

    @task.bash()
    def bash_command():
        return "echo teste_catchup , esse é um teste airflow para observar o catchup."
    

    bash_command()

dag_instance=task_definition()

