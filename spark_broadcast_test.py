#!/usr/bin/env python
# coding=utf-8
# @author 18099099
# spark广播测试
from pyspark import SparkContext, Row
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
import time
import datetime
import redis


def test(x):
    dict = x.asDict()
    df = pd.DataFrame(dict.values(), columns=['cnt'], index=pd.to_datetime(dict.keys())).sort_index()
    print(df.head())

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

datas = []
data = pd.read_msgpack(r.get("time_series"))
print(data.head())
dts = pd.DataFrame(data['count'].values.astype(np.str), index=pd.to_datetime(data['time'].values).astype(np.str))
dict = dts.to_dict(orient='dict')[0]
datas.append(dict)
spark = SparkSession.builder.appName("spark_broadcast_test").master("local[*]").getOrCreate()
spark.createDataFrame(datas).rdd.map(lambda x : test(x)).collect()


