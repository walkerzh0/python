#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
 
# ��һ���ļ�
fo = open("foo1.txt", "a")
#fo = open("foo1.txt", "w")


fo.write( "www.runoob.com!\nVery good site!\n")
 
# �رմ򿪵��ļ�
fo.close()

##!/usr/bin/python
## -*- coding: UTF-8 -*-
# 
## ��һ���ļ�
#fo = open("foo.txt", "w")
#print "�ļ���: ", fo.name
#fo.write( "www.runoob.com!\nVery good site!\n")
#print "�Ƿ��ѹر� : ", fo.closed
#print "����ģʽ : ", fo.mode
#print "ĩβ�Ƿ�ǿ�Ƽӿո� : ", fo.softspace


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