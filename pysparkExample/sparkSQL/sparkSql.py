from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)


lines = sc.textFile("file:///C:/data/fakefriends2.csv")
print(lines.first())
print(lines.count())
print(lines.map(lambda x: x+1))




# A DataFrame is a distributed collection of data organized into named columns. Spark SQL supports automatically converting an RDD containing case
# classes to a DataFrame with the method toDF():
# // change ebay RDD of Auction objects to a DataFrame
# val auction = ebay.toDF()