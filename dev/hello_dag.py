from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator


default_args = {
    'owner'                 : 'Mostafa Ghadimi',
    'description'           : 'Use of the DockerOperator',
    'depend_on_past'        : False,
    'start_date'            : datetime(2023, 4, 4),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}

with DAG('hello-world-2', default_args=default_args, schedule_interval="5 10 * * *", catchup=False) as dag:
    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "hello world"'
    )

t1