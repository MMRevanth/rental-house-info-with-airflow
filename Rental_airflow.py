from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Revanth',
    'depends_on_past': False,
    'start_date': datetime(2019,12,5),
    'email': ['mmrevanth00@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG('Renatal House', default_args=default_args, schedule_interval=timedelta(days=1))

def scrap():






t1 = PythonOperator(
    task_id='Scrap',
    python_callable=scrap,
    dag=dag)

t2 = SqliteOperator(house_list.sql,sqlite_conn_id='sqlite_default')

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag)

t2.set_downstream(t1)
t3.set_downstream(t2)



