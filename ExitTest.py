#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-25 10:30:13
# @File : ExitTest.py
# @Software : IntelliJ IDEA
import logging
import sys


def exit_normal():
    print "start exit ..."
    sys.exit(0)

def exit_error():
    print "start exit error ..."
    try:
        sys.exit(1)
    except Exception as e:
        logging.log(e)

if __name__ == '__main__':
    #exit_normal()
    exit_error()