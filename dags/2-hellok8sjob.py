from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['samuele.cozzi@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'hello_k8s_job', default_args=default_args, schedule_interval=timedelta(minutes=10))


start = DummyOperator(task_id='run_this_first', dag=dag)

# passing = KubernetesPodOperator(namespace='default',
#                           image="Python:3.6",
#                           cmds=["Python","-c"],
#                           arguments=["print('hello world')"],
#                           labels={"foo": "bar"},
#                           name="passing-test",
#                           task_id="passing-task",
#                           get_logs=True,
#                           dag=dag
#                           )

passing = KubernetesPodOperator(namespace='jobs-samuele-cozzi',
                          image="docker.io/samuelecozzi/job-sample:0.0.2",
                          labels={"foo": "bar"},
                          name="passing-test",
                          task_id="passing-task",
                          get_logs=True,
                          dag=dag
                          )



passing.set_upstream(start)