#!usr/bin/python
#coding=utf-8


print "whileѭ������"
number = 6
while number >= 0:
	#print "��",;print number,;print "ѭ��"	#ok
	print "��",number,"��ѭ��"				#ok
	number-=1
raw_input("waiting1....")


number = "haha"
number = 7			#ok pythonһ�������ڲ�ͬʱ��,���Ը�ֵΪ��ͬ��ֵ
while number>=0 :
	number-=1
	if(1 == number):
		break
	if(4 == number):
		continue
	print number		
raw_input("waiting2....")

print "forѭ������"
print "forѭ�����Ա����κ�����,��list��string" 
print "��ʽ1��ֱ�ӳ�Ա����"
for letter in 'Python':     # ��һ��ʵ��
   print '��ǰ��ĸ :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # �ڶ���ʵ��
   print '��ǰˮ�� :', fruit
   
   
print "��ʽ2����������"
index = 0
for index in range(len(fruits)):
	print "��ǰˮ��",fruits[index]
	
print "for...else...������"
for num in range(10,20):  # ���� 10 �� 20 ֮�������
   for i in range(2,num): # �������ӵ���
      if num%i == 0:      # ȷ����һ������
         j=num/i          # ����ڶ�������
         print '%d ���� %d * %d' % (num,i,j)
         break            # ������ǰѭ��
   else:                  # ѭ���� else ����
      print num, '��һ������'
	  
print "ѭ��Ƕ�ײ���"
i = 2
while(i < 10):
   j = 2
   while(j <= (i/j)):
      if not(i%j):
		  print "��",i
		  break
      j = j + 1
   print "xxx111��",i
   if (j > i/j) : print i, " ������"
   print "xxx��",i
   i = i + 1

print "Good bye!"
raw_input("xxxxxxxxxxxxxxxx")


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      # ���n��ż����ִ��continue���
        continue        # continue����ֱ�Ӽ�����һ��ѭ����������print()��䲻��ִ��
    print(n)
	
raw_input("hahahhahah")



