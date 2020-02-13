import os
import time
import itools

class LogTool:
    log_top_path = "find /storage/sdcard0/"
    logs = []

    def __init__(self):
        self.mOs = itools.Os()
        self.logs_saved_path = " E:\oppo\logs"
    def get_kernel_log(self):
        result = self.mOs.popen('adb shell find /storage -name *kernel_log*')

        #for line in result.read():         #此种读取方式，每次读一个字符
            #cmd = "adb pull " + line + " E:\oppo\logs"
            #self.mOs.popen(cmd)
            #print('lkl', cmd, 'done')
        idx = 0
        for idx in range(4):
            ret = result.readline()
            #print('lkl ', ret)
            cmd = "adb pull " + ret.strip() + se                                                        lf.logs_saved_path
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

class CmdObj:
    def __init__(self, cmdname):
        self.cmdname = cmdname
        self.cmdhelp = {}
    def parser(self, cmd_input):
        pass
    def handler(self):
        pass
    def help(self):
        print('this is cmd not helpinfo')

class VersionCmdObj(CmdObj):
    def __init__(self):
        super().__init__('version')
        self.logserver_path = 'G:\Workspaces\python\prjs\dir\logserver\prjs\\'
        self.comserver_path = 'G:\Workspaces\python\prjs\dir\comserver\prjs\\'
        print('cmdname: ', self.cmdname)
    def parser(self, cmd_input):
        print('cmd_input:', cmd_input)
    def handler(self):
        prjs = os.listdir(self.comserver_path)      # compile_server
        items = os.listdir(self.logserver_path)     # log_server

        print('com服务器prjs:', self.comserver_path)
        for src_idx in range(prjs.__len__()):
            print(src_idx, ': ', prjs[src_idx])

        print('log服务器items:', self.logserver_path)
        for dst_idx in range(items.__len__()):
            print(dst_idx, ': ', items[dst_idx])

        # select copy param
        src_idx = input('版本原地址：')
        dst_idx = input('版本目的地址：')
        src_idx1 = int(src_idx)
        dst_idx1 = int(dst_idx)
        print('src_idx1, dst_idx1', src_idx1, dst_idx1)

        # wrap and exec cmd
        frm = self.comserver_path + prjs[src_idx1] + '\out\product\product_x\\bootimg.txt'
        to = self.logserver_path + items[dst_idx1]
        cmd = 'copy ' + frm + ' ' + to
        print('cmd:', cmd)
        itools.Os().popen(cmd)
        cmd = 'copy ' + self.logserver_path + 'VersionInfo.txt ' + to + '\VersionInfo.txt'
        itools.Os().popen(cmd)

        # notify user to prepare next event
        time.sleep(10)
        itools.Os().popen('notepad ' + to + '\VersionInfo.txt')

    def help(self):
        print('cmd version used to copy version between logserver and compile server')
        # print()

class CmdManager:
    def __init__(self):
        self.itwalk_cmdlist = ['version', 'log', 'rtcbug', 'patch', 'feature', 'issue', 'helper']
        self.cmd_obj_list =[]
        self.cmd_obj_list.append(VersionCmdObj())

    def handler(self, cmdname):
        for cmd_obj in self.cmd_obj_list:
            if cmdname == cmd_obj.cmdname:
                cmd_obj.parser(cmdname)
                cmd_obj.handler()

    def helper(self):
        for cmd in self.itwalk_cmdlist:
            print(cmd)

#mCmdManager = CmdManager()
#cmd_input = input('请输入命令：')
#mCmdManager.handler(cmd_input)

logtool = LogTool()
logtool.get_kernel_log()


# mLogTool = LogTool()
# mLogTool.get_kernel_log()
# path = 'G:\Workspaces\python\prjs\\'
# filename = 'LogInfo.txt'

# mLogTool.open_txtfile(path + filename)
# mLogTool.open_dir(path)
