#!/usr/bin/python
#coding=utf-8

#����������

class Cat:
	def __init__(self, name):
		self.name = name
	def eat(self):
		print "Сè����"
		
	def drink(self):
		print "Сè��ˮ"
	
	def printInfo(self):
		print "Name is ", self.name
tom = Cat("tom")			#��ִ���ұ�,��������,����tom���øö���
tom.eat()
tom.drink()
jarr.printInfo()

jarr = Cat("jarr")			#��ִ���ұ�,��������,����jarr���øö���
jarr.eat()
jarr.drink()
jarr.printInfo()
#����jarr��tom������һ������

print "jonh = jarr"
jonh = jarr
jonh.printInfo()

jonh.name = "haha"
jarr.printInfo()
#����jarr��jonh��ͬһ������

#������һ������Cat����

raw_input("waiting ...")


