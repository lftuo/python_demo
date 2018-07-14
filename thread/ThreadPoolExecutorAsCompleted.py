#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/7/14 下午12:47
# @File : ThreadPoolExecutorAsCompleted.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# ThreadPoolExecutor判断线程执行结束的方法：as_completed
#   as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞.
#   在有某个任务完成的时候，会yield这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。
#   从结果也可以看出，先完成的任务会先通知主线程。
from concurrent.futures import ThreadPoolExecutor,as_completed
import time

# 参数times用来模拟网络请求时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=4)
urls = [13, 4, 11, 2]
all_task = [executor.submit(get_html, (url)) for url in urls]

for feature in as_completed(all_task):
    data = feature.result()
    print("in main: get page {}s success".format(data))