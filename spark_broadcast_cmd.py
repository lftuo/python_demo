#!/usr/bin/env python
# coding=utf-8
# @author 18099099
import os
cmd = 'source change_spark_version spark-2.1.0 && /home/bigdata/software/spark-2.1.0.7-bin-2.4.0.10/bin/spark-submit ' \
      '--master yarn-cluster --num-executors 4 ' \
      '--conf spark.hadoop.mapreduce.output.fileoutputformat.compress=false ' \
      '--executor-memory 4g spark_broadcast_test.py'
os.system(cmd)