#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/7/26 上午8:17
# @File : LogicTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import mlflow
import mlflow.sklearn
import pandas as pd
import pymysql
import warnings
import numpy as np
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.linear_model import LogisticRegression as LR

warnings.filterwarnings("ignore")

# 打开数据库连接
db = pymysql.connect("localhost","root","123456","test" )
sql = "select * from bankloan"
data = pd.read_sql(sql,db)
x = data.iloc[:,:8].values
y = data.iloc[:,8].values

rlr = RandomizedLogisticRegression()
rlr.fit(x, y)
rlr.get_support()
mlflow.sklearn.log_model(rlr,"model_rlr")
print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
print(u'通过随机逻辑回归模型筛选特征结束。')


print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
x = data[data.columns[rlr.get_support()]].as_matrix()
lr = LR()
lr.fit(x, y)
score = lr.score(x, y)
predicted_qualities = lr.predict(x)
mlflow.log_metric("score", score)
mlflow.sklearn.log_model(lr, "model")
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为：%s' % lr.score(x, y))
print("Model saved in run %s" % mlflow.active_run().info.run_uuid)

