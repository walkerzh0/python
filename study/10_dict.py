#!/usr/bin/python
#coding=utf-8

print "�ɶ�"
temp_dict = {1:"haha", "chengdu":"dujiangyan", 3:"xinyuanweidianzi", 1:"hello", "huawei":"5G"}
print temp_dict

print "�ֵ��ӡ"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict

print "�ֵ����"
dict['Age'] = 8 # ����
dict['School'] = "RUNOOB" # ���
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print dict

print "ɾ���ֵ����"
del dict["Name"]
print dict
dict.clear()
print dict
del dict
print dict

print "�ֵ�d\n"
y = "xyz"
z = 10
d = {(2,):"hello", "hh":{1:"dict1", "x":y}}
print d
print "fhjfa",z
#print "d["hh"]: ",d["hh"]		#error
print "d[\"hh\"]: ",d["hh"]		#ok

e = d["hh"]
print "dict e is", e

print type(e)



raw_input("wating ....")

