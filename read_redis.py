#!/usr/bin/env python
# coding=utf-8
# @author 18099099
import redis
import pandas as pd

r = redis.Redis(host = '127.0.0.1', port = 6379, db = 0)
# r.zadd('zset_name1', b1=10, b2=5)
# for i in r.smembers("myset"):
#     print i
#
# print r.zcard("zset_name1")
# print r.zcount("zset_name1", 1,10)
# aa = r.zrange("zset_name1", 0, 1)
# print aa
# print(r.zrank("zset_name1", "b2"))
# print(r.zrevrank("zset_name1", "b2"))
# print(r.zscore("zset_name1", "b2"))

# data20180901 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180901", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
# data20180901.time =  pd.to_datetime(pd.to_datetime('20180901' + data20180901.time.str.replace(':','')))
# df20180901 = data20180901[['time','count']].sort_values(by=['time']).reset_index(drop=True)
# print list(df20180901['time'].values), list(df20180901['count'].values)
# for i, j in zip(list(df20180901['time'].values), list(df20180901['count'].values)):
#      times= pd.to_datetime(i)
#      r.zadd('time_series', str(times)=str(j))
#      print pd.to_datetime(times),j

# r.set("time_series", df20180901.to_msgpack(compress='zlib'))

data20180901 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180901", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180902 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180902", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180903 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180903", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180904 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180904", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180905 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180905", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180906 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180906", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180907 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180907", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180908 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180908", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180909 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180909", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])
data20180910 = pd.read_csv("/Users/tuotuo/Documents/suning/data/20180910", sep='\t', names=["time","count","host_cn","ip_cn","custon_cn","city_cn","day"])

data20180901.time =  pd.to_datetime(pd.to_datetime('20180901' + data20180901.time.str.replace(':','')))
data20180902.time =  pd.to_datetime(pd.to_datetime('20180902' + data20180902.time.str.replace(':','')))
data20180903.time =  pd.to_datetime(pd.to_datetime('20180903' + data20180903.time.str.replace(':','')))
data20180904.time =  pd.to_datetime(pd.to_datetime('20180904' + data20180904.time.str.replace(':','')))
data20180905.time =  pd.to_datetime(pd.to_datetime('20180905' + data20180905.time.str.replace(':','')))
data20180906.time =  pd.to_datetime(pd.to_datetime('20180906' + data20180906.time.str.replace(':','')))
data20180907.time =  pd.to_datetime(pd.to_datetime('20180907' + data20180907.time.str.replace(':','')))
data20180908.time =  pd.to_datetime(pd.to_datetime('20180908' + data20180908.time.str.replace(':','')))
data20180909.time =  pd.to_datetime(pd.to_datetime('20180909' + data20180909.time.str.replace(':','')))
data20180910.time =  pd.to_datetime(pd.to_datetime('20180910' + data20180910.time.str.replace(':','')))


df20180901 = data20180901[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180902 = data20180902[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180903 = data20180903[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180904 = data20180904[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180905 = data20180905[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180906 = data20180906[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180907 = data20180907[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180908 = data20180908[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180909 = data20180909[['time','count']].sort_values(by=['time']).reset_index(drop=True)
df20180910 = data20180910[['time','count']].sort_values(by=['time']).reset_index(drop=True)

r.set("time_series_20180901", df20180901.to_msgpack(compress='zlib'))
r.set("time_series_20180902", df20180902.to_msgpack(compress='zlib'))
r.set("time_series_20180903", df20180903.to_msgpack(compress='zlib'))
r.set("time_series_20180904", df20180904.to_msgpack(compress='zlib'))
r.set("time_series_20180905", df20180905.to_msgpack(compress='zlib'))
r.set("time_series_20180906", df20180906.to_msgpack(compress='zlib'))
r.set("time_series_20180907", df20180907.to_msgpack(compress='zlib'))
r.set("time_series_20180908", df20180908.to_msgpack(compress='zlib'))
r.set("time_series_20180909", df20180909.to_msgpack(compress='zlib'))
r.set("time_series_20180910", df20180910.to_msgpack(compress='zlib'))
