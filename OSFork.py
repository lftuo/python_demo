#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-25 10:36:14
# @File : OSFork.py
# @Software : IntelliJ IDEA
import os,sys,time

print "loli"
#print os.getpid()
pid = os.fork()
print pid
print "lolita"
if pid != 0:
    print "old pid",os.getpid()
    sys.exit(0)
os._exit(0)
print os.getpid()