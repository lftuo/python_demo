#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018-1-2 15:31:38
# @File : Selection.py
# @Software : IntelliJ IDEA
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

print '-----------------------------Getting----------------------------------'
print df['A']
print '\n'
print df[0:3]
print '\n'
print df['20130102':'20130104']

print '-----------------------------Selection by Label----------------------------------'
print df.loc[dates[0]]
print '\n'
print df.loc[:,['A','B']]
print '\n'
print df.loc['20130102':'20130104',['A','B']]
print '\n'
print df.loc['20130102',['A','B']]
print '\n'
print df.loc[dates[0],'A']
print '\n'
print df.at[dates[0],'A']

print '-----------------------------Selection by Position----------------------------------'
print df.iloc[3]
print '\n'
print df.iloc[3:5,0:2]
print '\n'
print df.iloc[[1,2,4],[0,2]]
print '\n'
print df.iloc[1:3,:]
print '\n'
print df.iloc[:,1:3]
print '\n'
print df.iloc[1,1]
print '\n'
print df.iat[1,1]
print '-----------------------------Boolean Indexing----------------------------------'
print df[df.A > 0]
print '\n'
print df[df > 0]
print '\n'
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print df2
print '\n'
print df2[df2['E'].isin(['two','four'])]
print '-----------------------------Setting----------------------------------'
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print s1
print '\n'
df['F'] = s1
print df
print '\n'
df.at[dates[0],'A'] = 0
print df
print '\n'
df.iat[0,1] = 0
print df
print '\n'
df.loc[:,'D'] = np.array([5] * len(df))
print df
print '\n'
print '-----------------------------Missing Data----------------------------------'
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print df1
print '\n'
df1.loc[dates[0]:dates[1],'E'] = 1
print df1
print '\n'
df1.dropna(how='any')
print df1
print '\n'
df1.fillna(value=5)
print df1