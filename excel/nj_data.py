#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/9/24 下午7:22
# @File : nj_data.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import xlrd
import pymysql

db = pymysql.connect("localhost","root","123456","xls_data" )
cursor = db.cursor()

# 解析Excel:分类/标题/价格/地址/备注
data = xlrd.open_workbook('/Users/tuotuo/Downloads/nanjing.xlsx')
tables = data.sheets()
for tab in tables:
    nrows = tab.nrows
    for i in range(nrows):
        if i == 0:
            print('---------------------------------------')
            cls = tab.row_values(i)[0]
            print(cls)
            print('---------------------------------------')
        elif i == 1:
            pass
        else:
            title = tab.row_values(i)[1]
            price = tab.row_values(i)[2]
            position = tab.row_values(i)[3]
            remark = tab.row_values(i)[4]
            print(title, price, position, remark)
            sql = """
                  INSERT INTO xls_data2(cls,title,price,position,remark)
                  VALUES(%s,%s,%s,%s,%s)
            """
            params = (cls, title, price, position, remark)
            cursor.execute(sql,params)
            db.commit()