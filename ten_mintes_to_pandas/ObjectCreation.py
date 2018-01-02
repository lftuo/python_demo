#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-2 14:45:29
# @File : ObjectCreation.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

# 使用默认的整型作为index
s = pd.Series([1,3,5,np.nan,6,8])
print s
# 使用时间作为index
dates = pd.date_range('20130101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print df

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print df2
print df2.dtypes

