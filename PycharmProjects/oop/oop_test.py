#!/usr/bin/python3
#coding=utf-8

class Dog(object):
    def __init__(self, name):
        self.name = name
        print("init %s ...." % self.name)

    def play(self):
        print("%s 在普通狗玩耍" % self.name)


class XiaoTianQuan(Dog):
    def play(self):
        super().play();
        print("%s 也可以在天上玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name
        print("class Person %s init ..." % self.name)

    def paly_with_dog(self, dog):
        print("%s 在和 %s 玩耍" % (self.name, dog.name))
        dog.play()


wangcai = Dog("wangcai")
#wangcai.play()
xtq = XiaoTianQuan("xiaotianquan")
#xtq.paly()

xiaoming = Person("xiaoming")

xiaoming.paly_with_dog(xtq)
xiaoming.paly_with_dog(wangcai)


