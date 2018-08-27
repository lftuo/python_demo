#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/8/2 下午8:54
# @File : excel.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# python解析Excel
import xlrd
import pymysql

db = pymysql.connect("localhost","root","123456","xls_data" )
cursor = db.cursor()

# 解析Excel
data = xlrd.open_workbook('/Users/tuotuo/Downloads/touhang_doc.xls')
tables = data.sheets()
for tab in tables:
    nrows = tab.nrows
    for i in range(nrows):
        #try:
        if i == 0:
            continue
        area = tab.row_values(i)[0]
        title = (tab.row_values(i)[1]).replace('：', '').replace(' ','/').replace('，','/')
        detail_area = (tab.row_values(i)[2]).replace('：', '').replace(' ','/').replace('，','/')
        info_src = (tab.row_values(i)[3]).replace('：', '').replace(' ','/').replace('，','/')
        num = (tab.row_values(i)[4]).replace('：', '').replace(' ','/').replace('，','/')
        age = (tab.row_values(i)[5]).replace('：', '').replace(' ','/').replace('，','/')
        quality = (tab.row_values(i)[6]).replace('：', '').replace(' ','/').replace('，','/')
        waixing = (tab.row_values(i)[7]).replace('：', '').replace(' ','/').replace('，','/')
        fuwuneirong = (tab.row_values(i)[8]).replace('：', '').replace(' ','/').replace('，','/')
        price = (tab.row_values(i)[9]).replace('：', '').replace(' ','/').replace('，','/')
        job_time = str(tab.row_values(i)[10]).replace(' ','/').replace('，','/')
        env = (tab.row_values(i)[11]).replace('：', '').replace(' ','/').replace('，','/')
        safety = (tab.row_values(i)[12]).replace('：', '').replace(' ','/').replace('，','/')
        qq_tel = (tab.row_values(i)[13]).replace('：', '').replace(' ','/').replace('，','/')
        zhpj = (tab.row_values(i)[14]).replace('：', '').replace(' ','/').replace('，','/')
        mark = (tab.row_values(i)[15]).replace('：', '').replace(' ','/').replace('，','/')

        sql = """
                  INSERT INTO xls_data1(area,title,detail_area,info_src,num,age,quality,waixing,fuwuneirong,price,job_time,env,safety,qq_tel,zhpj,mark)
                  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        params = (area,title,detail_area,info_src,num,age,quality,waixing,fuwuneirong,price,job_time,env,safety,qq_tel,zhpj,mark)
        cursor.execute(sql,params)
        db.commit()
        #except:
        #    print(area,title,detail_area,info_src,num,age,quality,waixing,fuwuneirong,price,job_time,env,safety,qq_tel,zhpj)


