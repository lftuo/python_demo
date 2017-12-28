#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-25 09:50:33
# @File : ArgsTest.py
# @Software : IntelliJ IDEA
def foo_args(*args):
    print args

def foo_kwargs(x,**kwargs):
    print (x)
    print kwargs

def foo_all_args(x,*args,**kwargs):
    '''

    :param x: 位置参数
    :param args:
    :param kwargs:
    :return:
    '''
    print x
    print args
    print kwargs

if __name__ == '__main__':
    #foo_args(1,2,3,4)
    #foo_kwargs(1,y=1,a=2,b=3,c=4)
    foo_all_args(1,2,3,4,y=1,a=2,b=3,c=4)