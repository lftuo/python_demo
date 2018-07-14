#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/7/14 下午12:25
# @File : SimpleThreadPoolExecutor.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# ThreadPoolExecutor的简单应用
from concurrent.futures import ThreadPoolExecutor
import time

# 参数times用来模拟网络请求时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=4)

# 通过submit函数提交执行函数到线程池中，submit函数不会立即返回，不阻塞
task1 = executor.submit(get_html, (13))
task2 = executor.submit(get_html, (8))
task3 = executor.submit(get_html, (3))
task4 = executor.submit(get_html, (2))


# done方法用于判断某个线程是否执行完
print(task1.done())
print(task2.done())
print(task3.done())
print(task4.done())
# cancel方法用于取消某个任务，该任务没有放入线程池中才能取消成功
print(task2.cancel())
time.sleep(4)
print(task1.done())
print(task2.done())
print(task3.done())
print(task4.done())
# result方法用于获取线程池的执行结果
print(task1.result())