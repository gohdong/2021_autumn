import findspark
findspark.init()
from pyspark import SparkContext

sc = SparkContext("local","quiz 1")


input_rdd = sc.textFile("input.txt")
input_rdd.first()