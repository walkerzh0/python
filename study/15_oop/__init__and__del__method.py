#!usr/bin/python
#coding=utf-8

class Cat:
	def __init__(self, name):
		self.name = name
		print("__init__ %s " % self.name)
		
	def __del__(self):
		print("__del__ %s " % self.name)
		
tom = Cat("Tom")
print "haha end"

del tom				#__del__������16��֮ǰ����
print "--"*20


raw_input("waiting ...")

#���û��15�д���,__del__��19��֮�����,��Ϊtom��һ��ȫ�ֶ���,ֻ�е������������,ȫ�ֶ�������������ڲŻ��ս�