#!/usr/bin/python
#coding=utf-8

print "string usstrge\t\t","哈哈\f"		#\v：纵向制表符,\t:横向制表符
#print "\b"								#\b:退格
str = 10
print "hello",str						#ok:hello 10
#print "hello"+str						#error
print "hello",str*2						#ok:hello 20
str = "world"
print "hello",str*2						#ok:hello worldworld
print "hello" + str						#ok:helloworld

print "字符串引用与截取 []使用方法"
print str
print str[1]
print str[:2]
print str[1:3]

print "in,not in usage"
x = 'y'
if('y' in str):
	print "y in " + str
elif x not in str:
	print x + " not in " + str

print "原始字符串使用方法"
print R'\n\r'
print r'\b\n\r'

print "格式化字符串%"
print "My name is %s and weight:%d, age:%d, addess:%s" % ('Zara', 21, 33, "汉中") 
	
print "三引号案例"
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print errHTML
	
raw_input("wstrting end ....")
