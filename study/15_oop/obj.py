#!/usr/bin/python
#coding=utf-8

#对象与引用

class Cat:
	def __init__(self, name):
		self.name = name
	def eat(self):
		print "小猫吃鱼"
		
	def drink(self):
		print "小猫喝水"
	
	def printInfo(self):
		print "Name is ", self.name
tom = Cat("tom")			#先执行右边,创建对象,在用tom引用该对象
tom.eat()
tom.drink()
jarr.printInfo()

jarr = Cat("jarr")			#先执行右边,创建对象,在用jarr引用该对象
jarr.eat()
jarr.drink()
jarr.printInfo()
#以上jarr和tom并不是一个对象

print "jonh = jarr"
jonh = jarr
jonh.printInfo()

jonh.name = "haha"
jarr.printInfo()
#以上jarr和jonh是同一个对象

#本例中一共两个Cat对象

raw_input("waiting ...")


