#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/8/23 下午5:20
# @File : ParquetTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# 写csv文件

import codecs
import pandas as pd

# file = codecs.open('test.csv','w','utf-8')
# file.write('id,name,age\n')
# file.write('1,zhangsan,18\n')
# file.write('2,lisi,28\n')
#
# df = pd.read_csv("/Users/tuotuo/Documents/codes/python_demo/pands/test.csv")
# print(df)


head = ["id" , "name" , "age"]
l = [[1 , 'zhangsan' , 22],[2, 'lisi', 6] , [3 , 'wangwu' , 19], [4 , 'zhaoliu' , 26]]
df = pd.DataFrame (l , columns = head)
print(len(df))
print(df)
df.to_csv ("testfoo.csv" , encoding = "utf-8")
dfxx = pd.read_csv("testfoo.csv",encoding='utf-8')
dfxx.to_parquet("test.parquet",engine='pyarrow')
fi = codecs.open("test.parquet", 'r', encoding='utf-8')
print(fi.stream.read())