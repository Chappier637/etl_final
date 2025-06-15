from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("create-table") \
    .enableHiveSupport() \
    .getOrCreate()

csv_file_path = 's3a://dataproc-bucket222/transactions_v2.csv'
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Запись датафрейма в бакет в виде таблицы countries
df.write.mode("overwrite").option("path","s3a://dataproc-bucket222//transactions").saveAsTable("transactions")
