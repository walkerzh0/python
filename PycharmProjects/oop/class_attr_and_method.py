#!/usr/bin/python3
#coding=utf-8

class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def getCnt(cls):
        print("count = %d" % Tool.count)
        #return Tool.count              #ok
        return cls.count                #ok

    @staticmethod
    def showInfo():
        print("我是一个工具类")

tool1 = Tool("剪刀")
tool2 = Tool("刀叉")
tool3 = Tool("铲子")
print("Tool count is %d" % Tool.count)
Tool.getCnt()
Tool.showInfo()