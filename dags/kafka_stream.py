from datetime import datetime
from airflow import DAG
from airflow .operators.python import PythonOperator

default_args = {
    'owner':'airscholar',
    'strart_date':datetime(2013,8,3,10,00)
}

def stream_data():
    import requests
    import json

    res = requests.get("https://randomuser.me/api/")
    print(res.json())


""" with DAG('user_automation',
        default_args=default_args,
        schedule_interval='@daily',
        catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
 """
##dssdsd
stream_data()