#!/usr/bin/python3
#coding=utf-8

class A:
    def ptintInfoA(self):
        print("我是A类")
        pass

class B:
    def printInfoB(self):
        print("我是B类")
        pass

class C(A, B):
    def test(self):
        print("C自己的test方法")
        pass

c = C()
c.ptintInfoA()
c.printInfoB()
c.test()