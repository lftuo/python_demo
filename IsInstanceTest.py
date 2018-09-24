#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/9/20 上午10:28
# @File : IsInstanceTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# Isinstance的用法是用来判断一个量是否是相应的类型，接受的参数一个是对象加一种类型。
a = 1
print(isinstance(a, int))
print(isinstance(a, float))


# 其实，说的更为通用一些，isinstance是用于判断一个对象是否是一个类的实例的函数。为了说明其通用性，接下来再进行一个类以及对象的判断。
class Demo:

    pass


instDemo = Demo()
print(isinstance(instDemo, Demo))