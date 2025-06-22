import uuid
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator  # updated import

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 0)
}

def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    return res['results'][0]

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60:
            break
        try:
            res = get_data()
            res = format_data(res)
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

with DAG(
    dag_id='user_automation',
    default_args=default_args,
    start_date=datetime(2023, 9, 3),
    schedule='@daily',  
    catchup=False,
    tags=['user', 'kafka']
) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
