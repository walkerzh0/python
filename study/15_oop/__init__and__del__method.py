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

del tom				#__del__方法在16行之前调用
print "--"*20


raw_input("waiting ...")

#如果没有15行代码,__del__在19行之后调用,因为tom是一个全局对象,只有当整个程序结束,全局对象的是生命周期才会终结