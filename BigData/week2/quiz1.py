import findspark
findspark.init()
from pyspark import SparkContext

sc = SparkContext("local","quiz 1")

input_rdd = sc.textFile("input.txt")
flatten_rdd = input_rdd.flatMap(lambda l : l.split()).filter(lambda x:len(x)>=2)

print(input_rdd.first())