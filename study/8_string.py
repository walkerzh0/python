#!/usr/bin/python
#coding=utf-8

print "string usstrge\t\t","����\f"		#\v�������Ʊ��,\t:�����Ʊ��
#print "\b"								#\b:�˸�
str = 10
print "hello",str						#ok:hello 10
#print "hello"+str						#error
print "hello",str*2						#ok:hello 20
str = "world"
print "hello",str*2						#ok:hello worldworld
print "hello" + str						#ok:helloworld

print "�ַ����������ȡ []ʹ�÷���"
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

print "ԭʼ�ַ���ʹ�÷���"
print R'\n\r'
print r'\b\n\r'

print "��ʽ���ַ���%"
print "My name is %s and weight:%d, age:%d, addess:%s" % ('Zara', 21, 33, "����") 
	
print "�����Ű���"
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
