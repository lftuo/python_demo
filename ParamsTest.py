#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/8/29 下午3:51
# @File : ParamsTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
if 1 == 2:
    client = "test"
else:
    client = "test111"

if 'client' in vars() and client is not None:
    print(client)