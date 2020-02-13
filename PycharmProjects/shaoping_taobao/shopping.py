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
	time.sleep(15)
	#if driver.find_element_by_link_text("密码登录"):
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
	driver.get("https://cart.taobao.com/cart.htm")
	if driver.find_element_by_id("J_SelectAll1"):
		driver.find_element_by_id("J_SelectAll1").click()
	time.sleep(3)
	if driver.find_element_by_link_text("结 算"):
		driver.find_element_by_link_text("结 算").click();
	now = datetime.datetime.now()
	print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

##
##def login(username, password):
##    driver.get("https://passport.jd.com/new/login.aspx")
##    time.sleep(3)
##    driver.find_element_by_link_text("账户登录").click()
##    driver.find_element_by_name("loginname").send_keys(username)
##    driver.find_element_by_name("nloginpwd").send_keys(password)
##    driver.find_element_by_id("loginsubmit").click()
##    time.sleep(3)
##    driver.get("https://cart.jd.com/cart.action")
##    time.sleep(3)
##    driver.find_element_by_link_text("去结算").click()
##    now = datetime.datetime.now()
##    #now_time = now.strftime('%Y-%m-%d %H:%M:%S')
##    print(now.strftime('%Y-%m-%d %H:%M:%S'))
##    print('login success, you can ou up!')

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            #driver.find_element_by_id('order-submit').click()
            driver.find_element_by_link_text('提交订单').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
        time.sleep(0.5)

login('your_jd_username', 'your_jd_password')
buy_on_time('2019-03-14 10:00:00')




##-*- coding: UTF-8 -*-
#import os
#from selenium import webdriver
#import datetime
#import time
#
#chromedriver = "/usr/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)
#def login(uname, pwd):
#  driver.get("https://www.taobao.com")
#  if driver.find_element_by_link_text("亲，请登录"):
#    driver.find_element_by_link_text("亲，请登录").click();
#  time.sleep(1)
#  if driver.find_element_by_link_text("密码登录"):
#    driver.find_element_by_link_text("密码登录").click();
#  time.sleep(1)
#  if driver.find_element_by_name("TPL_username"):
#    driver.find_element_by_name("TPL_username").send_keys(uname);
#  time.sleep(1)
#  if driver.find_element_by_name("TPL_password"):
#    driver.find_element_by_name("TPL_password").send_keys(pwd);
#  time.sleep(2)
#  if driver.find_element_by_id("J_SubmitStatic"):
#    driver.find_element_by_id("J_SubmitStatic").click();
#  time.sleep(1)
#  driver.get("https://cart.taobao.com/cart.htm")
#  if driver.find_element_by_id("J_SelectAll1"):
#    driver.find_element_by_id("J_SelectAll1").click()
#  time.sleep(3)
#  if driver.find_element_by_link_text("结 算"):
#    driver.find_element_by_link_text("结 算").click();
#  now = datetime.datetime.now()
#  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
#def buy_on_time(buytime):
#  while True:
#    now = datetime.datetime.now()
#    if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
#      while True:
#        try:
#          driver.find_element_by_link_text('提交订单').click()
#        except:
#          time.sleep(1)
#    time.sleep(0.1)
##中文账号的时候要给它编码一下，不然会出错
#login("中文账号".decode('utf-8'),'密码')
#login("英文账号",'密码')
#buy_on_time('2017-05-06 21:30:01')