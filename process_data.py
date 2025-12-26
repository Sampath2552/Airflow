import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

if __name__ == "__main__":
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("Airflow-Spark-Job-2025-dabdidi") \
        .getOrCreate()

    print("Spark Session successfully started.")

    # Create dummy data for processing
    data = [("Alice", 34), ("Bob", 45), ("Charlie", 23)]
    columns = ["Name", "Age"]
    
    df = spark.createDataFrame(data, schema=columns)
    
    # Simple transformation
    result_df = df.withColumn("Status", lit("Processed-2025")) \
                  .filter(col("Age") > 25)

    print("Transformed Data:")
    result_df.show()

    # In a real scenario, you'd save this to HDFS or S3
    # result_df.write.mode("overwrite").parquet("/tmp/processed_data")

    spark.stop()
