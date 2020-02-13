#!usr/bin/python
#coding=utf-8

from selenium import webdriver
import datetime
import time

driver = webdriver.Firefox()
# http://gate.jd.com/InitCart.aspx?pid=4993737&pcount=1&ptype=1

def login(uname, pwd):
	driver.get("https://www.taobao.com")
	if driver.find_element_by_link_text("亲，请登录"):
		driver.find_element_by_link_text("亲，请登录").click();
	time.sleep(15)													#等待扫码登陆
	#if driver.find_element_by_link_text("密码登录"):				#下面这段为密码登录
	#	driver.find_element_by_link_text("密码登录").click();
	#time#.sleep(1)
	#if driver.find_element_by_name("TPL_username"):
	#	driver.find_element_by_name("TPL_username").send_keys(uname);
	#time.sleep(1)
	#if driver.find_element_by_name("TPL_password"):
	#	driver.find_element_by_name("TPL_password").send_keys(pwd);
	#time.sleep(2)
	#if driver.find_element_by_id("J_SubmitStatic"):
	#	driver.find_element_by_id("J_SubmitStatic").click();
	time.sleep(1)
	driver.get("https://cart.taobao.com/cart.htm")					#购物车页面
	if driver.find_element_by_id("J_SelectAll1"):
		driver.find_element_by_id("J_SelectAll1").click()
	time.sleep(3)
	if driver.find_element_by_link_text("结 算"):
		driver.find_element_by_link_text("结 算").click();
	now = datetime.datetime.now()
	print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:			#购买条件
            #driver.find_element_by_id('order-submit').click()
            driver.find_element_by_link_text('提交订单').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success....')
        time.sleep(0.5)

login('your_jd_username', 'your_jd_password')						#登录账户
buy_on_time('2019-03-14 10:00:00')
