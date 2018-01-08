#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-29 10:50:03
# @File : PythonAnalysis.py
# @Software : IntelliJ IDEA
import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt

conn= MySQLdb.connect(host='localhost',port = 3306,user='root',passwd='123456',db ='spider_lianjia',charset='utf8')
cur = conn.cursor()
sql = "SELECT city,area,avg(price) as avg_price FROM spider_lianjia.quanguo_xiaoqu_position_info where city = '南京' and price != '暂无' group by area"
df = pd.read_sql(sql,conn,index_col=('area'))
df.plot()
plt.show()