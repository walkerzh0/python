#!/usr/bin/python
#coding=utf-8

#number , string, Ԫ������ں����ڲ��޸Ĳ�Ӱ�캯�����,������C/C++��ֵ����
def exp_info_print(modid, exp_info) :
	"��ӡģ���쳣��Ϣ"
	print "[%s]:%s" % (modid, exp_info)
	modid = "charger"
	exp_info = "charger dect fail"
	print "*************************"

#dict��list�����ں����ڲ��޸Ļ�Ӱ�캯�����,�������ý�����������ɺ����޸ĺ��ֵ,������C/C++ַ����
def update_verify_info(province_dict) :
	"dict and list �������޸�,�������ý�����Ӱ����Ȼ����"
	if(province_dict["sichuan"] == "xian") :
		province_dict["sichuan"] = "chengdu"
		print "error:sichuan is chengdu"
		
#�����������ͣ��ر�����, �ؼ��ֲ���, Ĭ�ϲ���, ����������
#�ر�����
def must_param_fn_test(number):
	print "student number is��%d" % (number,)
	
#�ؼ��ֲ���
def key_param_fn_test(name, id) :
	print "Name, id: %s, %d" % (name, id)

#Ĭ�ϲ���,Ĭ�ϲ���һ��Ҫ���ں���	
#def key_param_default_fn_test(name = "zhangha0", id) :	#error
def key_param_default_fn_test(id, name = "zhangha0") :
	print "Name1, id: %s, %d" % (name, id)
	
#����������
def not_sure_fn_test(arg1, *arglist) :
	pass

#��������
yy = lambda x, y : x*y;


#return value
def get_add(x, y) :
	z = x + y
	return z
	
	
total = 242			#�˴�Ϊȫ�ֱ���
def local_global_var_test(x, y) :
	total = x + y
	print "local_global_var_test total is ", total
	return total	#�˴�Ϊ�ֲ�����,������ͬ����ȫ�ֱ���
	
print "�������ò���"
print "number, string, Ԫ��ֵ���ݲ���"
modid = "usb"
exp_info = "usb match device fail\n"
exp_info_print(modid, exp_info)
print modid
print exp_info

print "list, dictַ���ݲ���"
province_dict = {"sichuan":"xian", "shanxi":"xian"}
print "province_dict",province_dict
print "province_dict[\"sichuan\"] :",province_dict["sichuan"]
update_verify_info(province_dict)
print "province_dict",province_dict
print "province_dict[\"sichuan\"] :",province_dict["sichuan"]

print "������������"
must_param_fn_test(127)
key_param_fn_test(id = 784, name = "zhangha0")
key_param_default_fn_test(id=10)
not_sure_fn_test(1)

print "������������"
print "yy(20, 40) is ",yy(20, 40)

print "����return test"
print "get_add(3, 8)", get_add(3, 8)

print "�������������"
print "���br total is ", total
print "local_global_var_test(3, 6) is ", local_global_var_test(3, 6)
print "���af total is ", total


raw_input("waiting...")


	

