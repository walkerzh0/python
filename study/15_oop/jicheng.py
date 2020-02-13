#!usr/bin/python
#coding=utf-8

class Animal:
	def __init__(self):
		self.age = 100

	def eat(self):
		print "吃"
		
	def drink(self):
		print "喝"

	def eat(self):
		print "睡觉"		
		
		
class Dog(Animal):				#继承Animal
	def jump(self):
		print "蹦蹦跳跳"

	def run(self):
		print "跑"

	def bark(self):
		print "汪汪叫"
		
class XiaoTianQuan(Dog):	
	def fly(self):
		print "飞起来"
	def bark(self):				#方法重写
		"神狗的叫法"
	def run(self):				#方法扩展：既有父类的动作,也有子类特有的动作
		Dog.run(self)			#Python 2.7父类扩展方法
		#super().run()			#Python 3.0父类扩展方法
		print "驾云空中跑"
		
tom = Dog()
tom.eat()
tom.drink()
#tom.run()

xtq = XiaoTianQuan()
xtq.fly()
xtq.run()
xtq.jump()

print "继承爷爷辈属性测试:xtq age is %d" % xtq.age		#继承的传递性,可以继承爷爷辈的属性和方法


