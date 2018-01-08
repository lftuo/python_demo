#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/1/8 下午7:03
# @File : Categoricals.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# TODO 不懂
import pandas as pd
import numpy as np

# 类标签为[a, b, e]
df = pd.DataFrame({"id" : [1, 2, 3, 4, 5, 6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
print df
print '\n'
# 将raw_grade列转化为category类型
df["grade"] = df["raw_grade"].astype("category")
print df["grade"]
print '\n'
# 改变类别标签为[very good, good, very bad]
df["grade"].cat.categories = ["very good", "good", "very bad"]
print df["grade"]
print '\n'
# 改变类别标签集合，注意和上面的对.categories的操作进行区分。改变类别标签集合，操作过后数据的标签不变，但是标签的集合变为[“very bad”, “bad”, “medium”, “good”, “very good”]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print df["grade"]
print '\n'
# 按照类标签在标签集中的顺序排序，而不是安装类标签的字母顺序进行排序
print df.sort_values(by="grade")
print '\n'
# 根据类标签进行分组
print df.groupby("grade").size()
