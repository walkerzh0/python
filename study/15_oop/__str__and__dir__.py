#!/usr/bin/python
#coding=utf-8


class Dog:
	def __init__(self, name):
		self.name = name
		print "__init__ name is %s" % self.name
	def __del__(self):
		print "__del__ name is %s" % self.name
		
	def __str__(self):
		return "%s __str__" % self.name
		
mDog = Dog("xiaohei")
print(mDog)

dir(Dog)