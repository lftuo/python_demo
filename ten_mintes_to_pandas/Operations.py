#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-2 17:00:31
# @File : Operations.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print '-----------------------------Stats----------------------------------'
print df.mean()
print '\n'
print df.mean(1)
print '\n'
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print s
print '\n'
print df.sub(s, axis='index')
print '-----------------------------Apply----------------------------------'
print df.apply(np.cumsum)
print '\n'
print df
print df.apply(lambda x: x.max() - x.min())
print '-----------------------------Histogramming----------------------------------'
s = pd.Series(np.random.randint(0, 7, size=10))
print s
print s.value_counts()
print '-----------------------------String Methods----------------------------------'
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print s.str.lower()