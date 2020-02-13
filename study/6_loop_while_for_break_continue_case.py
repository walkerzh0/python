#!usr/bin/python
#coding=utf-8


print "while循环测试"
number = 6
while number >= 0:
	#print "第",;print number,;print "循环"	#ok
	print "第",number,"次循环"				#ok
	number-=1
raw_input("waiting1....")


number = "haha"
number = 7			#ok python一个变量在不同时刻,可以赋值为不同的值
while number>=0 :
	number-=1
	if(1 == number):
		break
	if(4 == number):
		continue
	print number		
raw_input("waiting2....")

print "for循环测试"
print "for循环可以遍历任何序列,如list或string" 
print "方式1：直接成员引用"
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
   
   
print "方式2：索引引用"
index = 0
for index in range(len(fruits)):
	print "当前水果",fruits[index]
	
print "for...else...语句测试"
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
	  
print "循环嵌套测试"
i = 2
while(i < 10):
   j = 2
   while(j <= (i/j)):
      if not(i%j):
		  print "数",i
		  break
      j = j + 1
   print "xxx111数",i
   if (j > i/j) : print i, " 是素数"
   print "xxx数",i
   i = i + 1

print "Good bye!"
raw_input("xxxxxxxxxxxxxxxx")


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      # 如果n是偶数，执行continue语句
        continue        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
	
raw_input("hahahhahah")



