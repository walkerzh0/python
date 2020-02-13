#!/usr/bin/python
#coding=utf-8

print "成都"
temp_dict = {1:"haha", "chengdu":"dujiangyan", 3:"xinyuanweidianzi", 1:"hello", "huawei":"5G"}
print temp_dict

print "字典打印"
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict

print "字典更新"
dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print dict

print "删除字典操作"
del dict["Name"]
print dict
dict.clear()
print dict
del dict
print dict

print "字典d\n"
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

