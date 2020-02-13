# 打印
print("start python study: print Hello\n")

# 列表
print("# 列表及使用")
database = [
    ["Hello1", 1],
    ["Hello2", 2],
    ["Hello3", 3]
]

# 成员检查
print("# 成员检查")
if ["Hello2", 2] in database:
    print("Yes\n")

# 列表赋值，指向一块内存
print("# 列表赋值，指向一块内存")
db = database
print(db)
db[1] = [23, 333]
print(db)

# 列表操作与列表方法
print("# 列表操作与列表方法:append, extend, insert, clear, copy, sort, reverse")
# append, extend, insert, clear, copy, sort, reverse

# 简化的字符串格式
print("# 简化的字符串格式")
fmt = "Hello %s %d Haalal"
val = "World", 123                  # 元组
info = fmt % val
print(info)

# 字符串方法
print("字符串方法:center, join, split, lower, little, replace, strip")
# center, join, split, lower, little, replace, strip
str = "Hello"
str1 = str.center(20, "*")
print(str)
print(str1)
str1 = str.center(20)
print(str1)

str = ['1', '2', '3']
str1 = '/'.join(str)
print(str1)
str2 = str1.split('/')
print(str2)
str3 = "  sdkjvdsjkv  "
print(str3)
str4 = str3.strip()
print(str4)

print("# 断言与程序出错")
idx = 9
assert idx >= 0, "idx must morethan 0"

# if与while与for
print("# 程序结构:if、while、for、break、continue、while&True/break、pass、exec/eval、del与垃圾回收")
names = ["zhangsan", "lisi", 3]
idx = 0
while idx < names.__len__():
    print(names[idx])
    names[idx] = idx
    print("af" + (names[idx]).__str__())
    idx += 1

for name in names:
    name1 = name*3
    print(name1)

m = [1, 2, 3]
n = [4, 5, 6]
[print("%d*%d: %d", m1, n1, m1*n1) for m1 in m for n1 in n]

# exec("cd c:")
res = {}
exec("ret = 'dir'", res)
ret1 = res['ret']
print(ret1)

print("# 程序注释:func_name.__doc__")
def Hello():
    Hello.__doc__
    'Hello is a function used to say hello'
    print('Hello')


Hello()


xy = range(10)
print(xy)


# *与**与函数参数使用方法,如何通过参数传递及引用元组&字典
print("# *与**与函数参数使用方法,如何通过参数传递及引用元组&字典")
def f1(**param):
    print(param)


def f2(*param):
    print(param)


f1(x=1, y=3, z=6)
f2(1, 2, 3, 4, 5)


def f3(**param):
    print("name:" + param['name'] + " num:" + param['num'])


def f4(*param):
    len = 0
    while len < param.__len__():
        print(param[len])
        len += 1


f3(name="kaili", num="234")
f4(2, 3, 4, 8)


# 变量作用域：global x、global()['var_name']
print("# 变量作用域：global x、global()['var_name']")
gvar1 = -1
gvar2 = -2


def change_var():
    gvar1 = 10
    gvar2 = 2
    globals()['gvar2'] = 3
    print("func gvar1 = ", gvar1)
    print("func global()['gvar1'] = ", globals()['gvar1'])
    print("gvar2 = ", gvar2)

change_var()
print("gvar1 = %d" % gvar1)
print("gvar2 = %d" % gvar2)


def change_gvar():
    global gvar1
    gvar1 = 20
    print("change_gvar1 func = ", gvar1)


change_gvar()
print("change_gvar gvar1", gvar1)



print("# 嵌套函数，作用域")
def cont():
    conter = 0
    def incont():
        nonlocal conter
        conter += 1
        return conter
    conter += 1
    return incont

func = cont()
print('func', func())
print('func', func())
func1 = cont()
print('func1', func1())
print('func1', func1())
print('func', func())
print('func', func())





print("# 类/抽象/与面向对象编程")
print("# class define example")
class People:
    def talk(self):
        print("I am a people")

people = People()
people.talk()


print("# 继承与超类")
class Student(People):
    def talk(self):
        print("I am a student")
    def study(self):
        print("I'm study now")

st = Student()
st.talk()
st.study()
print("Student的基类是", Student.__bases__)
if issubclass(Student, People):
    print("Student继承自People,是People的子类")
if isinstance(st, Student) and isinstance(st, People):
    print("st是Student的实例,同时也是People的实例")

print("# 多重继承")
class People1:
    def talk(self):
        print("I am a people1")
class MidStudent(People1, Student):
    pass
class LittleStudent(Student, People1):
    pass

midst = MidStudent()
midst.talk()
midst.study()
little = LittleStudent()
little.talk()
little.study()

print("# 抽象基类")
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def run(self):
        pass

class Cow(Animal):
    def run(self):
        print("cow running......")
class Pig(Animal):
    def run(self):
        print("pig running......")

    def sing(self):
        print("pig sing luo luo ......")
        self.getName()

    def setName(self, name):
        self.name = name
    def getName(self):
        print("my name is ", self.name)

cow = Cow()
cow.run()

pig = Pig()
pig.run()
pig.setName("piqi")
pig.sing()

import os
def python_os_system():
    #infoList = os.system("dir G:\Workspaces\python\lianxi > G:\Workspaces\python\lianxi\dirlist.txt")
    #pingInfo = os.system("ping 127.0.0.1")
    #print("infoList:", infoList)
    #print(pingInfo)
    #os.system("cmd")
    infoList = os.listdir("G:\Workspaces\python\lianxi")
    print("infoList:", infoList)

python_os_system()

import comlib
comlib.sayHello()


print("# 文件使用")
def file_test(file, mode):
    # if isinstance(file, str):
    f = open(file, mode)
    print(" f = ", f)

    f.write("Hello, ")
    f.write("World!\n")
    f.close()

    f = open(file, 'r')
    str5 = f.read()
    f.close()
    #print(str5)


file_test("2.txt", 'w')

def ReadFileLines(filename):
    f1 = open(filename, 'r')

    lines = f1.readlines()
    for l in lines:
        print(l)
    f1.close()

    f3 = open("3.txt", 'w')
    f3.writelines(lines)
    # f3.flush()
    f3.close()


ReadFileLines("2.txt")

def ProcessFile(filename, action):
    f = open(filename, 'r')
    fout = open("out.txt", 'a')

    while True:
        char = f.read()
        if char:
            fout.write(char.lower())
        else:
            break

ProcessFile("3.txt", 0)

x = 50
if 0 < x < 10:
    print('x is <0 to 10> ', x)
else:
    print('x is not <0 to 10>', x)

xy = range(10)
print('xy = ', xy)

xyz = 1
def xyz_test():
    global xyz
    xyz = 10
    print('xyz_test xyz', xyz)
    #print('xyz_test globle xyz', globals()['xyz'])

xyz_test()
print(xyz)

















