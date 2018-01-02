#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-2 15:14:57
# @File : ViewData.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print '-----------------------------df.head()----------------------------------'
print df.head()
print '-----------------------------df.tail(3)----------------------------------'
print df.tail(3)
print '-----------------------------df.index----------------------------------'
print df.index
print '-----------------------------df.columns----------------------------------'
print df.columns
print '-----------------------------df.values----------------------------------'
print df.values
print '-----------------------------df.describe()----------------------------------'
print df.describe()
print '-----------------------------df.T----------------------------------'
print df.T
print '-----------------------------df.sort_index----------------------------------'
print df.sort_index(axis=1, ascending=False)
print '-----------------------------df.sort_values----------------------------------'
print df.sort_values(by='B')