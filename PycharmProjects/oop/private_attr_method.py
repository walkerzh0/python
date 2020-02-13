#!/usr/bin/python3
#coding=utf-8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__id = 123
        self.age = age

    def showInfo0(self):
        print("父类共有方法访问私有属性__id")
        print ("__id is %d " % self.__id)


class Women(Person):
    def __secret1(self):
        print("%s age = %d" % (self.name, self.age))

    def secret(self):
        print("%s age = %d" % (self.name, self.age))


# def showInfo(self):
#	print "__id is ", self.__id			#不能访问父类私有属性和方法


xiaohong = Women("小红1", 45)
xiaohong.secret()
# xiaohong.__secret()		#私有方法不允许访问,类似的也是不能使用obj.private_attr访问的私有属性的
# xiaohong.showInfo()		#继承之后,子类方法同样不能访问父类私有属性,即不能继承父类的私有属性和私有方法
xiaohong.showInfo0()
print("-------------------")
mPersonObj = Person("comm", 78)
mPersonObj.showInfo0()