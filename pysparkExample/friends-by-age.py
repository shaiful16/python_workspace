from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf = conf)

#
# def parseLine(line):
#     fields = line.split(',')
#     age = int(fields[2])
#     numFriends = int(fields[3])
#     return (age, numFriends)
#
# lines = sc.textFile("file:///C:/data/fakefriends2.csv")
# rdd = lines.map(parseLine)
# totalsByAge = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
#
# results = totalsByAge.collect()
# for result in results:
#     print(result)


# data = [   {'id':1},{'id':2}   ]
# distData = sc.parallelize(data)
# totalsByAge = distData.mapValues(lambda x: (x, 1))
# results = totalsByAge.collect()
# for result in results:
#     print(result)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)



print( distData.reduce(lambda a, b: a + b) )