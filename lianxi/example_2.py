#!/usr/bin/python
#coding=utf-8

print "һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룻�����£������ڵ�10�����ʱ�������������ף���10�η�����ߣ�"

i = 1
tmp = 0
heigh = 100
total = 0
for i in range(1, 11) :
	if 1 == i :
		tmp = 100
	else :
		tmp = heigh * (0.5 ** (i - 1))
		if i == 10 :
			print "10th is ", heigh * (0.5 ** i)
		tmp *= 2
	total += tmp
	
print "total is ", total


raw_input("1, 2, 3, 4....")