#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2018/6/5 下午3:24
# @File : CopyFileUtil.py
# @Software : IntelliJ IDEA
# @Email ： 909709223@qq.com
# 1.将A文件复制到B文件中去(保持原来格式)
def copy_file (inputFile, outputFile, encoding):
    fin = open(inputFile, 'r', encoding=encoding) #以读的方式打开文件
    fout = open(outputFile, 'w', encoding=encoding) #以写得方式打开文件
    i = 0;
    for eachLiine in fin.readlines(): #读取文件的每一行
        i = i+1
        #if(i == 100):
        if(i == 87):
            print(eachLiine)
            line = eachLiine.strip() #去除每行的首位空格
            fout.write(line + '\n')
            i = 0
    fin.close()
    fout.close()



if __name__ == '__main__':
    copy_file('/Users/tuotuo/Documents/GitHub/dga_classifier/vectorized_feature_w_ranks_norm.txt','/Users/tuotuo/Documents/GitHub/dga_classifier/vectorized_feature_w_ranks_norm_copy_test.txt','UTF-8')
    #contents = read_file_list('../dict/time.dict','UTF-8')
    #print(contents)