from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark import SQLContext



conf = SparkConf().setMaster("local").setAppName("people")
sc = SparkContext(conf = conf)
sparkSession =SparkSession(sc);

df = sparkSession.read.json("file:///C:/data/people.json")

# Displays the content of the DataFrame to stdout
df.show()