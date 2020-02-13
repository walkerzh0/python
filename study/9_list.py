#!/usr/bin/python
#coding=utf-8

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
print "list1[1:3]: ",list1[1:3]

list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
list.append('Runoob1')
list.append('Runoob2')
list[2] = 33
print list
del list[2]
print list

raw_input("waiting...")
