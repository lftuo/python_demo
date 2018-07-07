#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/7/7 下午9:22
# @File : DateDiff.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import time
import datetime
t1 = datetime.datetime.now()
time.sleep(30)
t2 = datetime.datetime.now()
interval_time = (t2 - t1).seconds
print(interval_time)