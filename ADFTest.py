#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/9/20 下午2:47
# @File : ADFTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# adf检验是用来检验序列是否平稳的方式
# 一般来说是时间序列中的一种检验方法
# python中可使用现成的工具statsmodels来实现adf检验

import numpy as np
import statsmodels.tsa.stattools as ts

