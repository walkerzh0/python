#!/usr/bin/python
#coding=utf-8

print "一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"

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