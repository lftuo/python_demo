#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/1/8 下午9:43
# @File : Plotting.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# print ts
# 累积型的函数：此处为计算正态分布的累加值，化成曲线图
# ts = ts.cumsum()
# ts.plot()
# plt.show()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
# plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()