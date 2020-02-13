#!/usr/bin/python
#coding=utf-8

#ok
#from print_support import print_time
#print_time("2019-03-03")

#error
#from print_support import print_time		#ok
#print_support.print_time("2019-03-03")		#error:print_support no define

#ok
import print_support
print_support.print_info("world!\n")
print_support.print_time("2019-03-03")


Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print Money
AddMoney()
print Money


raw_input("module_test waiting .....")

