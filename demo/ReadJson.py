#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/1/3 下午8:06
# @File : ReadJson.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# 读取JSON文件
import json

with open('city.json', 'r') as json_file:
    data = json.load(json_file)


#for x in data:
#    print x['city'],x['code']
start_urls = []

for i in data:
    start_urls.append("https://%s.fang.lianjia.com/loupan/rs/"%i['code'])

for x in  start_urls:
    print x
