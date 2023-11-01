import pandas as pd
import numpy as np
import pyspark
import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
from pyspark import SQLContext
from pyspark.sql.types import StructType, StructField, FloatType, BooleanType, IntegerType, StringType

conf = pyspark.SparkConf()
spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark_sql = SQLContext(spark)

schema = StructType([
StructField("User ID", IntegerType(),True),
StructField("Username", StringType(),True),
StructField("Browser", StringType(),True),
StructField("OS", StringType(),True),
])

data = ([(1580, "Barry", "FireFox", "Windows" ),
(5820, "Sam", "MS Edge", "Linux"),
(2340, "Harry", "Vivaldi", "Windows"),
(7860, "Albert", "Chrome", "Windows"),
(1123, "May", "Safari", "macOS")
])

#df = spark.sql("select 'spark' as hello ")
#df2 = spark.sql.createDataFrame
df2 = spark_sql.createDataFrame(data,schema)
df3 = spark.sql("select 'test' as test")
df2.show()