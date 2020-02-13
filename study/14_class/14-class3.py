#!/usr/bin/python
#coding=utf-8

class Person :
	age = 30
	heigh = 170
	
	#def __init__(self, name, heigh) :
	#	self.name = name
	#	self.heigh = heigh
	
	def __init__(self, name,heigh) :
		self.name = name

	
	def showInfo(self) :
		print "name = {}, age = {}, heigh = {}".format(self.name, self.age, self.heigh)
		
		
p1 = Person("hh", 172)
p2 = Person("gg", 173)
#Person.heigh = 189

print(p1.heigh, p2.heigh, Person.heigh)

raw_input("hahahahha")