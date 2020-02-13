#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
 
# 打开一个文件
fo = open("foo1.txt", "a")
#fo = open("foo1.txt", "w")


fo.write( "www.runoob.com!\nVery good site!\n")
 
# 关闭打开的文件
fo.close()

##!/usr/bin/python
## -*- coding: UTF-8 -*-
# 
## 打开一个文件
#fo = open("foo.txt", "w")
#print "文件名: ", fo.name
#fo.write( "www.runoob.com!\nVery good site!\n")
#print "是否已关闭 : ", fo.closed
#print "访问模式 : ", fo.mode
#print "末尾是否强制加空格 : ", fo.softspace


fo.close()

os.mkdir("newdir")

raw_input("waiting11 xxx ...")


#import os
#
#file = open("./newdir/test.txt", "w")
#
#file.close()
#
#raw_input("waiting ...")