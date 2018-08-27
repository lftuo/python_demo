#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/8/16 上午9:17
# @File : UseDemo.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
from func.FuncDemo import FuncDemo
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()
# 函数调用
rslt = FuncDemo.calc(iris)
print(rslt)