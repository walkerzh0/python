#!/usr/bin/python
#coding=utf-8

print "���ĸ����֣�1��2��3��4������ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�"
i = 0
j = 0
k = 0
for i in range(1,5) :
	for j in range(1,5) :
		for k in range(1,5) :
			if i != j and j != k and i != k :
				print "%d%d%d " % (i, j, k) 

raw_input("1, 2, 3, 4....")