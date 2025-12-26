from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='pyspark_job_trigger_v3',
    default_args=default_args,
    schedule=None,  # Manual trigger
    catchup=False,
    tags=['spark', '2025'],
) as dag:

    # Triggering the PySpark script via spark-submit
    run_spark_task = SparkSubmitOperator(
        task_id='run_pyspark_process',
        # Path inside the Airflow Worker container
        application='/opt/airflow/dags/process_data.py',
        # Must match the Connection ID set in the Airflow UI
        conn_id='spark_default',
        name='airflow_pyspark_execution',
        verbose=True,
        # conf={
        #     "spark.master": "spark://spark-master:7077",
        #     # "spark.submit.deployMode": "client"
        # }
    )

    run_spark_task