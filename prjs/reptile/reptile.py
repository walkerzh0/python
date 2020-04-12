print('reptile爬虫学习与数据分析')
import requests
from bs4 import BeautifulSoup
#payload = {'wd': 'python'}
#r = requests.get('http://www.baidu.com/', params=payload)
r = requests.get('https://www.python.org/')
print(r.url)
print(r.encoding)
print(r.status_code)
#print(r.text)
f = open('html.html', 'w', encoding='utf-8')
f.write(r.text)
f.close()

f = open('html.html', 'rb')
html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
#a_list = soup.find_all('a', class_="jump-link")
#len = a_list.__len__()
#print('a lable len is ', len)
#idx = 0
for idx in range(4):
    print('item ', idx,  'is :', soup.find_all('a', class_="jump-link")[idx].get_text())
    idx = idx + 1

###########################################################################
print('selenium异步请求使用')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('http://www.python.org')
assert 'Python' in driver.title
print('Title is ', driver.title)
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('Pycon')
elem.send_keys(Keys.RETURN)
driver.close()