#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
counter = 100 # ��ֵ���ͱ���
miles = 1000.0 # ������
name = "John" # �ַ���
 
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

print list               # ��������б�
print list[0]            # ����б�ĵ�һ��Ԫ��
print list[1:3]          # ����ڶ�����������Ԫ�� 
print list[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinylist * 2       # ����б�����
print list + tinylist    # ��ӡ��ϵ��б�
print "\n"

print "tuple test"
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

#list[0:3] = 90			 #error 
#tuple[0] = 90			 #error:tuple only read

print tuple               # ��������б�
print tuple[0]            # ����б�ĵ�һ��Ԫ��
print tuple[1:3]          # ����ڶ�����������Ԫ�� 
print tuple[2:]           # ����ӵ�������ʼ���б�ĩβ������Ԫ��
print tinytuple * 2       # ����б�����
print tuple + tinytuple    # ��ӡ��ϵ��б�





raw_input("hellll")






'''
#�ű����б�����#!/usr/bin/python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
counter = 100 # ��ֵ���ͱ���
miles = 1000.0 # ������
name = "John" # �ַ���
 
print counter
print miles
print name


input()
'''



