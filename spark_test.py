#!/usr/bin/env python
# coding=utf-8
# @author 18099099
from operator import add
from pyspark import SparkContext
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[1]").appName("time_series_ml").getOrCreate()
    # sc = SparkContext(appName="PythonWordCount")
    lines = spark.sparkContext.textFile("words.txt")
    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    spark.stop()