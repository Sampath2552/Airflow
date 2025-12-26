from pyspark.sql import SparkSession
import os

if __name__ == "__main__":
    # In cluster mode, the driver runs on a worker node.
    # The application name helps identify it in the Spark Master UI (localhost:8081).
    spark = SparkSession.builder \
        .appName("2025_Cluster_Mode_Job") \
        .getOrCreate()

    print("--- CLUSTER MODE EXECUTION START ---")
    
    # Simple data processing example
    data = [("Node", os.uname().nodename), ("Execution", "Cluster Mode")]
    df = spark.createDataFrame(data, ["Property", "Value"])
    
    df.show()
    
    # Log where this is running
    print(f"Driver is currently running on host: {os.uname().nodename}")
    
    spark.stop()
