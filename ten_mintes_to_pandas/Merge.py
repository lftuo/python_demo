#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-3 16:02:52
# @File : Merge.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))
print df

print '-----------------------------Concat----------------------------------'
pieces = [df[:3], df[3:7], df[7:]]
print pieces
print pd.concat(pieces)

print '------------------------------Join-----------------------------------'
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print left
print right
print pd.merge(left, right, on='key')

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print pd.merge(left, right, on='key')

print '------------------------------Append---------------------------------'
df = pd.DataFrame(np.random.randn(8,4), columns=['A','B','C','D'])
print df
s = df.iloc[3]
print s
print df.append(s, ignore_index=True)

