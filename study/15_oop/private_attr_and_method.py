#!/usr/bin/python
#coding=utf-8
class Person:
	def __init__(self):
		self.__id = 123
		
	def showInfo0(self):
		print "���๲�з�������˽������__id"
		#print "__id is %d " % self.__id

class Women(Person):
	def __init__(self, name):
		self.name = name
		self.age = 19

	def __secret1(self):
		print "%s age = %d" % (self.name, self.age)		
		
	def secret(self):
		print "%s age = %d" % (self.name, self.age)
		
	#def showInfo(self):
	#	print "__id is ", self.__id			#���ܷ��ʸ���˽�����Ժͷ���
		
		
xiaohong = Women("С��1")
xiaohong.secret()
#xiaohong.__secret()		#˽�з������������,���Ƶ�Ҳ�ǲ���ʹ��obj.private_attr���ʵ�˽�����Ե�
#xiaohong.showInfo()		#�̳�֮��,���෽��ͬ�����ܷ��ʸ���˽������,�����ܼ̳и����˽�����Ժ�˽�з���
xiaohong.showInfo0()
print "-------------------"
mPersonObj = Person()
mPersonObj.showInfo0()