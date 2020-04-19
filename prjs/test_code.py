class TestObj:
    def __init__(self):
        pass

    def test(self):
        li = ['d1', 'd2', 'd3', 6]
        target = 'd2_x'

        if target in li:
            print(target, 'is li a element')
        else:
            print(target, 'is not found')

# mTestObj = TestObj()
# mTestObj.test()


class LogTool:
    log_top_path = "find /storage/sdcard0/"
    logs = []

    def __init__(self):
        self.mOs = itools.Os()
        self.logs_saved_path = " E:\oppo\logs"
        self.issue_list = []
    def get_kernel_log(self):
        result = self.mOs.popen('adb shell find /storage -name *kernel_log*')

        #for line in result.read():         #此种读取方式，每次读一个字符
            #cmd = "adb pull " + line + " E:\oppo\logs"
            #self.mOs.popen(cmd)
            #print('lkl', cmd, 'done')
        idx = 0
        for idx in range(4):
            ret = result.readline()
            cmd = "adb pull " #+ ret.strip() + " " + self.logs_saved_path   # 此句如果adb端口不在就会报错                                                        lf.logs_saved_path
            self.mOs.popen(cmd)

        self.open_dir(self.logs_saved_path)
            #print(cmd)

    def get_mobile_log(self):
        pass

    def open_dir(self, dir):
        cmd = 'explorer ' + dir
        self.mOs.popen(cmd)

    def open_txtfile(self, file):
        cmd = 'notepad ' + file
        self.mOs.popen(cmd)


# test pass
# logtool = LogTool()
# logtool.get_kernel_log()


# mLogTool = LogTool()
# mLogTool.get_kernel_log()
# path = 'G:\Workspaces\python\prjs\\'
# filename = 'LogInfo.txt'

# mLogTool.open_txtfile(path + filename)
# mLogTool.open_dir(path)



#from xml.sax import make_parser
#parser = make_parser()
#print('xml sax is ok')

from xml.sax.handler import ContentHandler
from xml.sax import parse

class TaskInfoHandler(ContentHandler):
    def __init__(self, taskinfo):
        super().__init__()
        self.data = {}
        self.key = []
        self.value = ''
        self.taskinfo = taskinfo

    def startElement(self, name, attrs):
        # self.data
        self.keyvalues = attrs.values()
        # print(self.key)
        # print(name, attrs.keys())

    def characters(self, content):
        self.value = content
        # print('cont: ' + content)

    def endElement(self, name):
        keytext = ''.join(self.keyvalues)
        self.taskinfo[keytext] = self.value
        # print(keytext + ': ' + self.value)
        self.keyvalues = []
        self.value = ''

# test pass
taskinfo = {}
parse('G:\Workspaces\python\prjs\dir\\taskinfo.xml', TaskInfoHandler(taskinfo))
print(taskinfo)


print("三引号：")
print('''I'm a student, and my name is "hello world"''')

print("原始字符串")
print(r'''I'm so sorry !!! "current path is C:\nowposation"''')

print("unicode编码")
print('\u00c6')
print("\N{Cat}")
print("\N{Dog}")

print('列表操作')
print('列表元素访问:切片 && 索引 && 步长')
l = 'Hello'
print('l[0] = ', l[0])
print('l[-1] = ', l[-1])
print('l[0:2]', l[0:2])
print('l[-3:-2]', l[-3:-2])
print('l[-3:-1]', l[-3:-1])
print('l[1:-1]', l[1:-1])
print('l[1:5]', l[1:5])
print('步长与简写')
print('l[0:4:2]', l[0:4:2])
print('l[::4]', l[::4])
print('l[4::-2]', l[4::-2]) #步长为负数时候，左边索引需要比右边索引大
print('l[:2:-2]', l[:2:-2]) #步长为负数时候，左边索引需要比右边索引大

print('列表初始化：*代替循环')
print([0] * 10)
print([1] * 10)
print([None] * 10)

print('检查序列中是否存在某元素: in运算符')
print('l' in l)
print('x' in l)
print('llo' in l) #in运算符可以检查子字符串

print('列表操作：赋值 && 删除 && 切片修改')
data = [1, 3, 5, 2, 5]
str = list('HelloWorld')
print('data is ', data)
print('str is ', str)
del data[2]
print('data is ', data)
del data[1:3]
print('data is ', data)
data[1:] = [4, 5, 6, 9]
print('data is ', data)
str[-1] = ['d', ' ', 'python']
print('str is ', str)
print(''.join(''.join(str[-1])))
str[-1] = ['d python']
print('str is ', str)
str[-1] = 'd python'
print('str is ', str)
print(''.join(str))

print('list 关函数：copy && ')
print(str)
str1 = str.copy()
print(str1)
str1[0] = 'A'
print(str)
print(str1)

str2 = str1[:]
print('str2 is', str2)
str2[0] = 'BB'
print('str1 is', str1)
print('str2 is', str2)

print('data is ', data)
data1 = list(data)
print('data1 is ', data1)
data1[1] = 99
print('data is ', data)
print('data1 is ', data1)
data1[2] = [3, 4, 2]
print('data1 is ', data1)
print('data1.index([3, 4, 2]) is ', data1.index([3, 4, 2]))

print('利用pop && append函数实现栈和队列')
list_st = []
for idx in range(10):
    list_st.append(idx)
    print(list_st)
for idx in range(10):
    list_st.pop()
    print(list_st)

print('function remove')
data1.clear()
#data1 = []
#data1[:] = []
print('data1 is ', data1)
data1 = ['is ', 'has', 'am', 'do', 'to']
data1.remove('has')
print('data1 is ', data1)
data1.reverse()
print('data1 is ', data1)


print('字符串格式方法format的三种使用方法')
format = '%s and %s is our tl and pm'
value = ('leader ge', 'boss huang')
print(format % value)

print('{} and {} is my teacher'.format('段老师', '陈老师'))
print('{teacher} and {student} is talking...'.format(teacher="黄磊", student='赵薇'))
print('{1} and {1} is talking...'.format('黄磊', '赵薇'))
print('{} and {} is data'.format([1, 2, 3], (3, 6)))

print('字符串格式控制符')
print('data b is {data:f}'.format(data=1327))
print('data d is {data:d}'.format(data=1327))
print('data x is {data:x}'.format(data=1327))
print('data o is {data:o}'.format(data=1327))

width = 35
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print(header_fmt)
print(fmt)

print('字符串方法')
str = 'This is is a people'
str1 = str.replace('is', 'eez')
print(str1)

print('字典及使用：dict, clear, keys, values, update, pop, get, items')
l = [('name', 'name1'), ('age', 23), (34, 'midle')]
l2 = [('name', 'name2'), ('age', 8000)]
d = dict(l)
d2 = dict(l2)
print(d)
print(d.keys())
print(d.values())
d.update(d2)
print(d)
print(d.items()) #将字典中的键值对转换成列表，列表元素为元组
info = 'My info is Name:{name} and Age:{age}'.format_map(d2)
print(info)

print('python函数特有的参数特性:定义参数收集 && 调用参数分配')
def f(x, *parma):
    print(x, parma)
def f2(x, *parma_t, **param_d):
    print(x, parma_t, param_d)
def f3(x, *parma_t, y, z, **param_d):
    print(x, parma_t, y, z, param_d)

f(1, 2, 'hello', 5, 'world')
f2(34, 1242, 'H1N1', y = 'AK', z = 'AKM')
f3(1, 'e', 3, 5, 8, 9, 70, z = 37, id = '384', name='x_company', y = 77)    #定义的是位置参数，调用的时候可以指定为关键字参数

def f4(x, y, z, m = 3, n = 4):
    print(x, y, z, m + n)

param_t = (1, 2, 3)
param_d = {'n':8, 'm':9}
f4(*param_t, **param_d)
param = (5, ) * 2
print(param)

print('面向对象:多重继承 && 抽象基类')
class Animal:
    def sport(self):
        print('Animal sport...')

class People:
    def sport(self):
        print('People sport...')

    def work(self):
        print('work...')

    def talk(self):
        print('People talk....')

class Student(Animal, People):
    pass

class Teacher(People, Animal):
    pass

Student().sport()
Teacher().sport()

st = Student()
tea = Teacher()

print(hasattr(st, 'talk'))
print(hasattr(st, 'talk1'))

print(callable(getattr(tea, 'sport')))
print(callable(getattr(tea, 'talk')))

from abc import ABC, abstractmethod
class BusInterface:
    @abstractmethod
    def communicat(self):
        pass

class UsbInterface(BusInterface):
    def communicat(self):
        print('usb communicating...')

UsbInterface().communicat()

print('魔法方法，列表协议，list,dict,str的子类派生实现征需求,迭代器，生成器')
print('列表映射协议')
class MyList:
    def checkkey(self, key):
        if isinstance(key, int):
            return True
        else:
            return False

    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.len = 1
        self.changed = {}
    def __len__(self):
        return self.len

    def __setitem__(self, key, value):
        if self.checkkey(key):
            self.changed[key] = value
        else:
            print('__setitem__ key is invalid')

    def __getitem__(self, key):
        if self.checkkey(key):
            #if self.changed[key]:
                #print('data has changed, now is ', self.changed[key])
            #else:
            print('start key step is ', self.start, key, self.step)
            print(self.start + key * self.step)
            return self.start + key * self.step
        else:
            print('__getitem__ key is invalid')

mylist = MyList(1, 1)
mylist[1] = 2
mylist[4] = 8
print('mylist[4], mylist[20] is ', mylist[4], mylist[20])

print('迭代器的两种使用方法')

print('生成器yield和return区别')
class TestUnit:
    def __init__(self):
        self.listdata = [[93, 9, 3], [7, 24], [6]]

    def testYield(self):                #step exec
        for sublist in self.listdata:
            for element in sublist:
                yield element           #iter

    def testFunc(self):                 #next exec
        for sublist in self.listdata:
            for element in sublist:
                return element
print('testFunc 不可迭代：next exec')
ret = TestUnit().testFunc()
print('testFunc:item is ', ret)
print('testFunc:item is ', ret)
print('testFunc:item is ', ret)
print('testFunc:item is ', ret)
print('testFunc:item is ', ret)
print('testFunc:item is ', ret)
print('testYield可以迭代：step exec')
testIter = TestUnit().testYield()
print('testYield:item is ', testIter.__next__())
print('testYield:item is ', testIter.__next__())
print('testYield:item is ', testIter.__next__())
print('testYield:item is ', testIter.__next__())
print('testYield:item is ', testIter.__next__())
print('testYield:item is ', testIter.__next__())

import re
print("正则表达式 * + ?")
ret = re.match('.*ython', '——     python')
print('.*ython', ret.group())
ret = re.match('.+ython', '——     python')
print('.+ython', ret.group())
ret = re.match('p?ython', 'python')
print('p?ython', ret.group())
ret = re.match('p?ython', 'ython')
print('p?ython', ret.group())
#ret = re.match('p?ython', 'xython') #返回None
#print('p?ython', ret.group()) #会报错AttributeError: 'NoneType' object has no attribute 'group'

print('正则表达式 * {} [] 原始字符r')
ret = re.match(r'w*.python.org', 'ww.python.orghahah')
print('w*.python.org', ret.group())

ret = re.match(r'w{3}.python.org', 'www.python.orghahah')
print('w{3}.python.org', ret.group())

ret = re.match(r'w{3,}.python.org', 'wwww.python.orghahah')
print('w{3,}.python.org', ret.group())

ret = re.match(r'w{3,10}.python.org', 'wwww.python.orghahah')
print('w{3,10}.python.org', ret.group())

ret = re.match(r'w{3,10}.python.org', 'wwwwxpythonxorghahah')
print('w{3,10}.python.org', ret.group())

ret = re.match(r'w{3,10}\.python\.org', 'wwww.python.orghahah')
print('w{3,10}\.python\.org', ret.group())

ret = re.match(r'[a-zA-Z_]*\.python\.org', 'www_w.python.orghahah')
print('[a-zA-Z_]*\.python\.org', ret.group())

ret = re.match(r'[a-zA-Z_]*\.python\.org$', 'www_w.python.org')     #不会报错
print('[a-zA-Z_]*\.python\.org$', ret.group())

#ret = re.match(r'[a-zA-Z_]*\.python\.org$', 'www_w.python.orgXXX') #返回None
#print('[a-zA-Z_]*\.python\.org$', ret.group()) #因为有$表示结束，现在后面以XXX结尾，会报错AttributeError: 'NoneType' object has no attribute 'group'

print('''正则表达式转义字符:特使字符\. \d \w \s '\\n' \D \W \S等''')
ret = re.match(r'[a-zA-Z_]*\.python[\d]\.org$', 'www.python3.org')     #不会报错
print('[a-zA-Z_]*\.python[\d]\.org$', ret.group())

#ret = re.match(r'[a-zA-Z_]*\.python[\d]\.org$', 'www.pythonx.org')     #匹配失败
#print('[a-zA-Z_]*\.python[\d]\.org$', ret.group())

ret = re.match(r'[a-zA-Z_]*\.python[\D]\.org$', 'www.python&.org')     #匹配非数字
print('[a-zA-Z_]*\.python[\D]\.org$', ret.group())


ret = re.match(r'[a-zA-Z_]*\.python[\W]\.org', '_www.python&.orgas')     #匹配非数字
print('[a-zA-Z_]*\.python[\W]\.org', ret.group())

#ret = re.match(r'[a-zA-Z_]*\.python[\w]\.org', '_www.python&.orgas')     #匹配失败，&不属于单词字符
#print('[a-zA-Z_]*\.python[\w]\.org', ret.group())


ret = re.match(r'[a-zA-Z_]*\.python[\s]\.org', '_www.python .orgas')     #\s匹配空格 制表符 换行\n
print('[a-zA-Z_]*\.python[\s]\.org', ret.group())

print('正则表达式：| 与分组匹配')
ret = re.match(r'[a-zA-Z_]*\.python[\s]*\.org', '_www.python    .orgas')     #匹配多次
print('[a-zA-Z_]*\.python[\s]*\.org', ret.group())

ret = re.match(r'([a-zA-Z0-9]*)(@)(qq|163|162)(\.com$)', 'test@162.com')
print(ret)
print('[a-zA-Z0-9]*@(qq|163|162)\.com$', ret.group())
print('[a-zA-Z0-9]*@(qq|163|162)\.com$', ret.group(1))
print('[a-zA-Z0-9]*@(qq|163|162)\.com$', ret.group(2))
print('[a-zA-Z0-9]*@(qq|163|162)\.com$', ret.groups())

print('正则表达式diff match and search')
ret = re.search(r'email:\w*@(qq|gmail|163|162)\.com', 'info email:28463@gmail.com') # 搜索匹配，只要字符串中有符合特征的字符串就返回
print('search:', ret)
print('search', ret.group())

#ret = re.match(r'email:\w*@(qq|gmail|163|162)\.com', 'info email:28463@gmail.com') # 从开始匹配，所以匹配失败
#print('match:', ret)
#print('search', ret.group())

print('正则表达式：findall sub split')
ret = re.findall(r',\d*', ',999, c++ = 2342 php = 2342 python = ,9000')
print(ret)

ret = re.findall(r',\d*', ',999, php = 2342 python = ,9000')
print(ret)

data = '347'
ret = re.sub(r'\d+', data, 'cpython user cont = 27349')
print('re.sub ret is ', ret)

ret = re.split(r':| ', 'cpython:user cont = 27349')
print('re.split ret is ', ret)

print('贪婪和非贪婪模式')
ret = re.match(r'(.+?)\d+', 'cpython user cont = 27349')    #数量词+{m, n}后面加?   ->  非贪婪模式：尽可能少的匹配
print('re.match ret is ', ret.groups(1))

ret = re.match(r'(.+)\d+', 'cpython user cont = 27349')     #默认：贪婪模式
print('re.match ret is ', ret.groups(1))