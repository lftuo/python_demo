#!/usr/bin/env python
# coding=utf-8
# @author 18099099
from pyspark.sql import SparkSession
import pandas as pd
import json

dict1 = {"data" :{'2018-09-01 05:30:00': '1447930', '2018-09-01 19:46:00': '4510598'}}
dict2 = {"data" :{'2018-09-02 13:06:00': '3571514', '2018-09-02 03:09:00': '1993175'}}
dicts = [dict1, dict2]


def predict(x):
    print(x.asDict())

print(dicts)
spark = SparkSession.builder.appName("time_series_ml").master("local[1]").getOrCreate()
spark.createDataFrame(dicts).rdd.map(predict).collect()