from pyspark.sql import *
import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

if __name__ == "__main__":

    spark = SparkSession.builder \
                    .master("local[2]") \
                    .appName("Hello Spark") \
                    .getOrCreate()

    data_list = [
        ("Ravi", 20),
        ("David", 40),
        ("Abdul", 60)]

    df = spark.createDataFrame(data_list).toDF("Name", "Age")
    df.collect()
