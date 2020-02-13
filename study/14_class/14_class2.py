#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Person :
	total_num = 0
	def __init__(self, name = "kaili", addr = "liuba") :
		Person.total_num += 1
		self.name = name
		self.addr = addr
		#print "name, addr:%s, %s" % (self.name, self.addr)
		
		
	def printInfo(self) :
		print '{1}, {0}'.format(self.name, self.addr)
		print "printInfo name, addr:%s, %s" % (self.name, self.addr)

p1 = Person("kaili", "mianxian")
p1.printInfo()
raw_input("Person")


class Student(Person) :
	def __init__(self, num) :
		self.num = num
	
	def printInfo(self) :
		#print "name, addr, num: %s, %s, %d" % (self.name, self.addr, self.num)
		print "name, addr, num:%d" % (self.num)
		
st = Student(127)
st.printInfo()
raw_input("Student")
