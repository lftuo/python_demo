#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/9/26 上午10:35
# @File : TupleTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 1.创建空元组
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# 创建空元组
tup4 = ()

# 元组中只包含一个元素时，需要在元素后面添加逗号
tup5 = (20,)

# 2.访问元组
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 3.修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup6 = tup2 + tup3
print(tup6)

# 4.删除元组
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup : ")
try:
    print(tup)
except Exception as e:
    print(e)