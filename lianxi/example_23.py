#!/usr/bin/python
#coding=utf-8

print "´òÓ¡ÐÎ×´"


max_level = 4
for i in range(1, max_level + 1) :
	for k in range(1, max_level - i + 1) :
		print " ",
	for j in range(1, (2*i-1) + 1) :
		print "*",
	print "\n"
	
max_level -= 1
for i in range(1, max_level+1) :
	for j in range(1, i+1) :
		print " ",
	for k in range(1, 2*max_level - (2*i - 1) + 1) :
		print "*",
	print "\n"



raw_input("1, 2, 3, 4....")