#!usr/bin/python
#coding=utf-8

class Animal:
	def __init__(self):
		self.age = 100

	def eat(self):
		print "��"
		
	def drink(self):
		print "��"

	def eat(self):
		print "˯��"		
		
		
class Dog(Animal):				#�̳�Animal
	def jump(self):
		print "�ı�����"

	def run(self):
		print "��"

	def bark(self):
		print "������"
		
class XiaoTianQuan(Dog):	
	def fly(self):
		print "������"
	def bark(self):				#������д
		"�񹷵Ľз�"
	def run(self):				#������չ�����и���Ķ���,Ҳ���������еĶ���
		Dog.run(self)			#Python 2.7������չ����
		#super().run()			#Python 3.0������չ����
		print "���ƿ�����"
		
tom = Dog()
tom.eat()
tom.drink()
#tom.run()

xtq = XiaoTianQuan()
xtq.fly()
xtq.run()
xtq.jump()

print "�̳�үү�����Բ���:xtq age is %d" % xtq.age		#�̳еĴ�����,���Լ̳�үү�������Ժͷ���


