from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id='pyspark_cluster_mode_v1',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=['spark', 'cluster-mode'],
) as dag:

    submit_cluster_job = SparkSubmitOperator(
        task_id='submit_to_cluster',
        # Path must be identical on both Airflow and Spark Workers
        application='/opt/spark_scripts/cluster_job.py', 
        conn_id='spark_default',
        # Key change: driver runs on worker nodes
        deploy_mode='cluster', 
        name='airflow_cluster_job',
        conf={
            "spark.master": "spark://spark-master:7077",
            # Optional: ensure driver can find python
            "spark.pyspark.python": "python3" 
        },
        verbose=True
    )