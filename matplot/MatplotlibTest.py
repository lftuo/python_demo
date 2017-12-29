#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-12-29 10:24:27
# @File : MatplotlibTest.py
# @Software : IntelliJ IDEA
import matplotlib.pyplot as plt
'''
#plt.plot(np.arange(10))
fig = plt.figure()
#plt.show()
#figsize 有一些重要的选项，特别是figsize，规定的是图片保存到磁盘时具有一定大小的纵横比。
#plt.gcf()即可得到当前Figure的引用
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum(),'k--')


#fig.add_subplot 返回的对象是AxesSubplot对象，下面调用就可以了
_ = ax1.hist(np.random.randn(100),bins = 20,color = 'k',alpha = 0.3)
ax2.scatter(np.arange(30),np.arange(30) + 3 * np.random.randn(30))
plt.show()
'''
#由于Figure 和 subplot是一件非常常见的任务，于是出现了更为方便的方法（plt.subplots ),它可以创建一个新的Figure，
#并返回一个含有已创建的subplot对象的Numpy数组
fig,axes = plt.subplots(2,3)

#print fig
print axes[0][0]
#axes[0][0].hist(np.random.randn(100),bins = 20,color = 'k',alpha = 0.3)
plt.show()
#这是非常实用的，因为可以轻松地对axes数组进行索引，就好像一个是一个二维数组一样，例如
#axes[0,1].还可以通过sharex和sharey指定subplot具有相同的x轴和y轴。在比较相同范围的数据时，这是
#非常实用的，否则matplotlib会自动缩放各图表的界限。