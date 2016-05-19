#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

fo.write( "www.runoob.com!\nVery good site!\n");

print "-----------------------------"
# 关闭打开的文件
fo.close()
print "是否已关闭 : ", fo.closed

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read();
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()

#os.rename( "foo.txt", "test2.txt" )

print os.getcwd()