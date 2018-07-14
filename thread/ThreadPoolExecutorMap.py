#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/7/14 下午12:58
# @File : ThreadPoolExecutorMap.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# ThreadPoolExecutor判断线程执行结束的方法：map
#   使用map方法，无需提前使用submit方法，map方法与python标准库中的map含义相同，都是将序列中的每个元素都执行同一个函数。
#   代码中就是对urls的每个元素都执行get_html函数，并分配各线程池。
#   可以看到执行结果与上面的as_completed方法的结果不同，输出顺序和urls列表的顺序相同，
#   就算2s的任务先执行完成，也会先打印出13s的任务先完成，再打印2s的任务完成。
from concurrent.futures import ThreadPoolExecutor,as_completed
import time

# 参数times用来模拟网络请求时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=4)
urls = [13, 4, 11, 2]

for data in executor.map(get_html, urls):
    print("in main: get page {}s success".format(data))