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

mTestObj = TestObj()
mTestObj.test()








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