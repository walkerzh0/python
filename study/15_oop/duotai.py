#!usr/bin/python
#coding=utf-8


class Dog(object):
	def __init__(self, name):
		self.name = name
		print "init %s ...." % self.name
	def play(self):
		print "%s ����ͨ����ˣ" % self.name
		
class XiaoTianQuan(Dog):
	def paly(self):
		print "%s ��������ˣ" % self.name
		
class Person():
	def __init__(self, name):
		self.name = name
		print "class Person %s init ..." % self.name
		
	def paly_with_dog(self, dog):
		print "%s �ں� %s ��ˣ" % (self.name, dog.name)
		dog.play()
		
		
wangcai = Dog("wangcai")
wangcai.play()
xtq = XiaoTianQuan("xiaotianquan")
xtq.paly()

xiaoming = Person("xiaoming")

xiaoming.paly_with_dog(xtq)
xiaoming.paly_with_dog(wangcai)