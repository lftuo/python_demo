#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/9/26 下午2:41
# @File : DiffRestoreTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# 一价差分还原操作
import pandas as pd
time_series = pd.Series([2,4,3,5,6,7,4,5,6,3,2,4], index=pd.date_range(start='2000', periods=12, freq='a'))
print(time_series)
time_series_diff = time_series.diff(1).dropna()
print(time_series_diff)
time_series_restored = pd.Series([time_series[0]], index=[time_series.index[0]]).append(time_series_diff).cumsum()
print(time_series_restored)
print('--------------------------')
pd.Series([time_series[0]], index=[time_series.index[0]])