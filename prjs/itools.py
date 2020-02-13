import os

class Os:
    ret = -1
    def system(self, cmd):
        ret = -1
        ret = os.system(cmd)
        # print('system(cmd):', cmd, "ret:", ret)
        print('system exec: ' + cmd + ' ret:', ret)

    def popen(self, cmd):
        ret = os.popen(cmd)
        # print('popen(cmd):', cmd, "ret:", ret)
        print('popen exec: ' + cmd)
        return ret

# mOs = Os()

# cmd = "ping www.baidu.com"
# cmd = "dir *.py"
# cmd = "md dir"
# cmd = "rd dir"
# cmd = "xxx"
# cmd = 'tasklist'
# cmd = "start regedit"
# cmd = ""

#mOs.system(cmd)
# ret = mOs.popen(cmd)
# data = ret.read()
# print(ret)
# print(data)
# if data.find("学习问题解决记录.docx") != -1:
    # print('find 学习问题解决记录.docx')
# else:
    # print('not find 学习问题解决记录.docx')

# if data.find("以毫秒为单位") != -1:
    # print('find 以毫秒为单位')
# else:
    # print('not find 以毫秒为单位')
