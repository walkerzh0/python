#!/usr/bin/python
#coding=utf-8
name = "hello"
class Student :
	"this is class student"
	count = 0
	def __init__(self, name, num) :
		self.name = name
		self.num = num
		Student.count += 1			#���������,���д��������,�൱��c++ class��static����
		#self.count += 1			#�����¶����Լ��ı���,ͬ�����֮�䲻����
		
		print "new __init__ %s" % (self.__doc__,)
	
	def printInfo(self) :
		#global name
		#name = "hello"
		print "no self name %s" % (name,)
		print "self name, num, total:%s, %d, %d" % (self.name, self.num, self.count)
		print "Student name, num, total:%s, %d, %d" % (self.name, self.num, Student.count)
		
	def __del__(self) :
		print "%s -----------------> ������" % self.__class__.__name__

		
st1 = Student("lukaili", 12010127)
st1.printInfo()
st3 = st1
st4 = st3

#st2 = Student("zengxiyao", 12010128)
#st2.printInfo()

st5 = Student("stu 5", 12010128)
st5.printInfo()


st6 = Student("stu 6", 12010128)
st6.printInfo()


print "will del........"
#del st1
#print "af del st1........"
del st3
print "af del st3........"
del st4
print "af del st4........"

#print "total: %d %d %d" % (st1.count, st2.count, Student.count)
#print "total: %d %d %d" % (st1.count, Student.count)
print "sdbfdsjdskjfksd"

raw_input("waiting student....")

#�ű�ִ�����֮�����__del__�ͷŶ���,һ������,���ܱ����ö��ٴ�,ֻ�ܱ��ͷ�һ��

