#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print counter
print miles
print name


#number
print "number test",;print "a b c"

a = b = c = 1
a = 3
#del b
print b
print a
print c
print "\n\n\n"
#string
str = "01234567"

print "string test"
print str[3]				#3
print str[3 : 6]			#345
print str[5 :]				#567
print str[1:3] * 3			#121212
print str[1:4] + "hello"	#123hello	


print "list test"

 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

#list[0:3] = 90			 #error 
list[0] = 90			 #ok

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
print "\n"

print "tuple test"
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

#list[0:3] = 90			 #error 
#tuple[0] = 90			 #error:tuple only read

print tuple               # 输出完整列表
print tuple[0]            # 输出列表的第一个元素
print tuple[1:3]          # 输出第二个至第三个元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出列表两次
print tuple + tinytuple    # 打印组合的列表





raw_input("hellll")






'''
#脚本首行必须是#!/usr/bin/python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print counter
print miles
print name


input()
'''



