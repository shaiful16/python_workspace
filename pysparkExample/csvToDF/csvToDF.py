from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sparkContext = SparkContext(conf = conf)
sparkSession =SparkSession(sparkContext);

Employee_rdd = sparkContext.textFile("file:///C:/data/fakefriends2.csv")\
    .map(lambda line: line.split(","))

langPercentDF0 = sparkSession.createDataFrame([("Scala", 35), ("Python", 30), ("R", 15), ("Java", 20)])
langPercentDF1 = sparkSession.createDataFrame(Employee_rdd)

langPercentDF0.show()
print()
print()
langPercentDF1.show()




young = langPercentDF0.filter(langPercentDF0._2 < 21)

print()
print()
young.show()