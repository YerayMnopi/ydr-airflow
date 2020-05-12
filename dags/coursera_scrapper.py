from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'Coursera scrapper',
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)


coursera = KubernetesPodOperator(namespace='default',
                          image="belce/ydr-data-crawler",
                          name="passing-test",
                          task_id="coursera-scrapper-task",
                          get_logs=True,
                          dag=dag
                          )

