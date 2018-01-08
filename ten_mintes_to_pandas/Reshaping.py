#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-8 10:17:18
# @File : Reshaping.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

print '-----------------------------Stack-------------------------------'
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print df
df2 = df[:4]
print df2

stacked = df2.stack()
print stacked

print stacked.unstack()

print stacked.unstack(1)
print stacked.unstack(0)

print '--------------------------Pivot Tables------------------------------'
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
print df
# 不懂
print pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])