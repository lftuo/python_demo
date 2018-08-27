#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/8/27 下午3:17
# @File : MutilThreadingTest.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
import multiprocessing
import datetime

def calc(i):
    sum = 0
    for _ in range(100000000):
        sum += 1
    print(i,sum)


if __name__ == "__main__":

    start = datetime.datetime.now()

    # 定义同时至多起几个线程
    pool = multiprocessing.Pool(10)
    for i in range(10):
        pool.apply_async(calc,args=(i,))

    # 用来阻止多余的进程涌入进程池 Pool 造成进程阻塞。
    pool.close()
    # 方法实现进程间的同步，等待所有进程退出。
    pool.join()
    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)