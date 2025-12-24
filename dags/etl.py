from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import json


# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id='nasa_apod_postgres_etl',
    default_args=default_args,
    description='ETL pipeline to fetch NASA APOD data and load into Postgres',
    schedule='@daily',
    start_date=datetime(2025, 12, 24),
    catchup=False,
    tags=['nasa', 'etl', 'postgres'],
) as dag:
    
    # Step 1: Create table if doesn't exist
    @task
    def create_table():
        postgres_hook = PostgresHook(postgres_conn_id='postgres_default')
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """
        postgres_hook.run(create_table_sql)
        return "Table created successfully"

    # Step 2: Extract NASA API DATA
    @task
    def extract_apod():
        import requests
        url = 'https://api.nasa.gov/planetary/apod'
        params = {'api_key': 'DEMO_KEY'}
        response = requests.get(url, params=params)
        return response.json()

    # Step 3: Transform Data
    @task
    def transform_data(response):
        apod_data = {
            'title': response.get('title', 'N/A'),
            'explanation': response.get('explanation', 'N/A'),
            'url': response.get('url', 'N/A'),
            'date': response.get('date', 'N/A'),
            'media_type': response.get('media_type', 'N/A')
        }
        return apod_data

    # Step 4: Load Data into Postgres
    @task
    def load_data(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id='postgres_default')
        
        insert_sql = """
        INSERT INTO nasa_apod (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """
        postgres_hook.run(insert_sql, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type']
        ))
        return "Data loaded successfully"

    # Set task dependencies
    table_created = create_table()
    api_data = extract_apod()
    transformed = transform_data(api_data)
    loaded = load_data(transformed)
    
    table_created >> api_data >> transformed >> loaded

        