#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-28 11:08:29
# @File : PandsStudy.py
# @Software : IntelliJ IDEA
import numpy as np, pandas as pd

#1/Series的创建
#序列的创建主要有三种方式
#1）通过一维数组创建序列
arr1 = np.arange(10)
print arr1
print type(arr1)

s1 = pd.Series(arr1)
print s1
print type(s1)

print '-----------------------------------------'
#2）通过字典的方式创建序列
dic1 = {'a':10,'b':20,'c':30,'d':40,'e':50}
print dic1
print type(dic1)

s2 = pd.Series(dic1)
print s2
print type(s2)
#3）通过DataFrame中的某一行或某一列创建序列

print '-----------------------------------------'
# 2/DataFrame的创建
#数据框的创建主要有三种方式
#1）通过二维数组创建数据框
arr2 = np.array(np.arange(12)).reshape(4,3)
print arr2
print type(arr2)

df1 = pd.DataFrame(arr2)
print df1
print type(df1)
print '------------------------------------------'
#2）通过字典的方式创建数据框
# 以下以两种字典来创建数据框，一个是字典列表，一个是嵌套字典。
dic2 = {'a':[1,2,3,4],'b':[5,6,7,8],
        'c':[9,10,11,12],'d':[13,14,15,16]}
print dic2
print type(dic2)

df2 = pd.DataFrame(dic2)
print type(df2)
print df2

dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},
        'two':{'a':5,'b':6,'c':7,'d':8},
        'three':{'a':9,'b':10,'c':11,'d':12}}
print dic3
print type(dic3)

df3 = pd.DataFrame(dic3)
print df3
print type(df3)

print '-------------------------------------------'
#3）通过数据框的方式创建数据框
df4 = df3[['one','three']]
print df4

s3 = df3['one']
print s3
print type(s3)

print '-------------------------------------------'
# 数据索引index
# 1、通过索引值或索引标签获取数据
s4 = pd.Series(np.array([1,1,2,3,5,8]))
print s4
print type(s4)

print s4.index
print s4[5]

s4.index = ['a','b','c','d','e','f']
print s4['f']

print '-------------------------------------------'
# 2、自动化对齐
s5 = pd.Series(np.array([10,15,20,30,55,80]))
s5.index = ['a','b','c','d','e','f']
print s5['e']

#三、利用pandas查询数据


print '-------------------------------------------'
#四、统计分析
d1 = pd.Series(2*np.random.normal(size = 100)+3)
d2 = np.random.f(2,4,size = 100)
d3 = np.random.randint(1,100,size = 100)

print d1.count()
print d1.min()
print d1.max()
print d1.idxmin()
print d1.idxmax()
print d1.sum()
print d1.mean()