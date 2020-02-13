#!/usr/bin/python
#coding=utf-8

#number , string, 元组参数在函数内部修改不影响函数外边,类似于C/C++的值传递
def exp_info_print(modid, exp_info) :
	"打印模块异常信息"
	print "[%s]:%s" % (modid, exp_info)
	modid = "charger"
	exp_info = "charger dect fail"
	print "*************************"

#dict和list参数在函数内部修改会影响函数外边,函数调用结束后参数会变成函数修改后的值,类似于C/C++址传递
def update_verify_info(province_dict) :
	"dict and list 被函数修改,函数调用结束后影响依然存在"
	if(province_dict["sichuan"] == "xian") :
		province_dict["sichuan"] = "chengdu"
		print "error:sichuan is chengdu"
		
#函数参数类型：必备参数, 关键字参数, 默认参数, 不定长参数
#必备参数
def must_param_fn_test(number):
	print "student number is：%d" % (number,)
	
#关键字参数
def key_param_fn_test(name, id) :
	print "Name, id: %s, %d" % (name, id)

#默认参数,默认参数一定要放在后面	
#def key_param_default_fn_test(name = "zhangha0", id) :	#error
def key_param_default_fn_test(id, name = "zhangha0") :
	print "Name1, id: %s, %d" % (name, id)
	
#不定长参数
def not_sure_fn_test(arg1, *arglist) :
	pass

#匿名函数
yy = lambda x, y : x*y;


#return value
def get_add(x, y) :
	z = x + y
	return z
	
	
total = 242			#此处为全局变量
def local_global_var_test(x, y) :
	total = x + y
	print "local_global_var_test total is ", total
	return total	#此处为局部变量,会屏蔽同名的全局变量
	
print "函数调用测试"
print "number, string, 元组值传递测试"
modid = "usb"
exp_info = "usb match device fail\n"
exp_info_print(modid, exp_info)
print modid
print exp_info

print "list, dict址传递测试"
province_dict = {"sichuan":"xian", "shanxi":"xian"}
print "province_dict",province_dict
print "province_dict[\"sichuan\"] :",province_dict["sichuan"]
update_verify_info(province_dict)
print "province_dict",province_dict
print "province_dict[\"sichuan\"] :",province_dict["sichuan"]

print "函数参数测试"
must_param_fn_test(127)
key_param_fn_test(id = 784, name = "zhangha0")
key_param_default_fn_test(id=10)
not_sure_fn_test(1)

print "匿名函数测试"
print "yy(20, 40) is ",yy(20, 40)

print "函数return test"
print "get_add(3, 8)", get_add(3, 8)

print "变量作用域测试"
print "外边br total is ", total
print "local_global_var_test(3, 6) is ", local_global_var_test(3, 6)
print "外边af total is ", total


raw_input("waiting...")


	

