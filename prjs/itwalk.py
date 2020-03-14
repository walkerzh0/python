import os
import time
import itools
from pathlib import Path    #用于检测文件或目录是否存在

class CmdObj:
    def __init__(self, cmdname):
        self.cmdname = cmdname
        self.cmdhelp = {}
        self.Os = itools.Os()
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

class LogCmdObj(CmdObj):
    def __init__(self):
        super().__init__('log')
        self.logs_computer_path = "G:\Workspaces\python\prjs\dir\logs\\"
        self.logs_phone_path = '/storage/emulated/0/xxx_log/'
        self.issues = []
        #列出当前issue_list
        issue_list = os.listdir(self.logs_computer_path)
        for issue in issue_list:
            if issue.find('issue') != -1:
                self.issues.append(issue)
                print('logs:' + issue)

        print('cmdname: ', self.cmdname)

    def parser(self, cmd_input):
        print(cmd_input)
        self.actione = ''
        if cmd_input.find(' -k') != -1:
            self.actione = '-k'
        elif cmd_input.find(' -m') != -1:
            self.actione = '-m'
        elif cmd_input.find(' -a') != -1:
            self.actione = '-a'
        else:
            pass

        #select target dir
        self.list_issues()
        self.target_dir = ''
        target_idx = input('选择target issue idx:')
        target_postfix = input('log详细信息')
        self.target_dir = self.logs_computer_path  + self.issues[int(target_idx)] + '\\' + target_postfix + '\\'
        os.popen('md ' + self.target_dir)
        print(self.target_dir)


    def handler(self):
        print('handler......')


        print(self.actione)
        self.exec_cmd = ''
        if self.actione == '-k':
            adb_kernels = os.popen('adb shell find /storage -name *kernel_log*')
            print(adb_kernels)
            idx = 0
            while True:
                kernel_log_line = adb_kernels.readline()
                #print(kernel_log_line)

                self.exec_cmd = "adb pull " + kernel_log_line.strip() + " " + self.target_dir
                self.Os.popen(self.exec_cmd)

                if kernel_log_line.strip() == '':
                    print('kernel log获取结束')
                    self.Os.popen('explorer ' + self.target_dir)
                    break

    def list_issues(self):
        #print issues
        len = self.issues.__len__()
        print('issue len:', len)
        for idx in range(len):
            print(self.issues[idx])

        #select will save dir



    def help(self):
        print(self.cmdname + 'helpinfo:')

class CmdManager:
    def __init__(self):
        self.itwalk_cmdlist = ['version', 'log', 'rtcbug', 'patch', 'feature', 'issue', 'helper']
        self.cmd_obj_list =[]
        self.cmd_obj_list.append(VersionCmdObj())
        self.cmd_obj_list.append(LogCmdObj())

    def handler(self, cmd_input):
        #检查命令合法性
        def_cmd = ''
        for def_cmd in self.itwalk_cmdlist:
            if cmd_input.find(def_cmd) != -1:
                break
            else:
                pass

        for cmd_obj in self.cmd_obj_list:
            if def_cmd == cmd_obj.cmdname:
                cmd_obj.parser(cmd_input)
                cmd_obj.handler()

    def helper(self):
        for cmd in self.itwalk_cmdlist:
            print(cmd)

# test pass
# mCmdManager = CmdManager()
# cmd_input = input('请输入命令：')
# mCmdManager.handler(cmd_input)



class Tasks:
    def __init__(self, name, prename, mornitorpoint):
        self.name = name
        self.prename = prename
        self.location = mornitorpoint + name
        self.status_file = 'okay.txt'
        self.online_tasks = []                         #任务中当前在线任务

    def register_new_task(self):
        ts = os.listdir(self.location)
        for t in ts:
            #检查&注册新任务
            if t.find(self.prename) == 0:
                if t in self.online_tasks:
                    pass
                else:
                    self.online_tasks.append(t)
                    print('new task: ', t, ' onlined')

    def list_task(self):
        ts = os.listdir(self.location)
        for task in ts:
            print(self.name, task)
            if task.find(self.prename) == 0:
                self.online_tasks.append(task)
                print(task, 'is inited')

    def check_task(self):
        for task in self.online_tasks:
            task_status = Path(self.location + '\\' + task +  '\\' + self.status_file)
            if task_status.exists():
                # print(self.location + '\\' + task + '\completed')
                # self.notify('please deal with task:' + self.name + '\\' + task)
                self.handler(self.location + '\\' + task + '\\')
                #self.notify(self.location + '\\' + task + '\\')

    def handler(self, info):
        print('Tasks handler ' + info + '......')

    def notify(self, info):
        print(info)

class TimerTasks(Tasks):
    def __init__(self, mornitorpoint):
        super().__init__('timertasks', 'tm_', mornitorpoint)

    # def list_task(self):
    #     print('list_task', self.location)
    # 
    # def check_task(self):
    #     print('check_task', self.location)
    # 
    # def notify(self, info):
    #     print('notify', info)

class BuildTasks(Tasks):
    def __init__(self, mornitorpoint):
        super().__init__('buildtasks', 'bd_', mornitorpoint)
        self.info_file = "completeinfo.txt"
        self.notify_file = '版本修改及验证说明.txt'
        self.notifyflag_file = 'notify complete.txt'
        self.outdir = 'out\\target\product\\' + 'platform_x\\'

    # def list_task(self):
    #     print('list_task', self.location)
    #     #ts = os.listdir(self.location)
    # 
    # def check_task(self):
    #     print('check_task', self.location)
    #

    def handler(self, taskpath):
        # print('BuildTask complete', taskpath)
        flag_file = Path(taskpath + '\\' + self.notifyflag_file)
        if flag_file.exists():      # 已通知过用户
            pass
        else:                       # 处理任务，并通知用户
            # read completeinfo.txt
            info_file = taskpath + self.info_file
            info = ''
            if Path(info_file).exists():
                finfo = open(info_file, 'r')
                info = finfo.read()
                finfo.close()

                # deal and write info into notify file
                info = info + ' \n' * 5 + '修改点: ' + ' \n' * 5

                #parser and copy version to target dir
                #print(info.find('out'))  # 返回目标字符串的索引
                tmpstr = info.split('\n')
                srcdir = (tmpstr[0].split(' '))[1]
                dstdir = tmpstr[2].split(' ')[1]

                cmd_cpboot = 'copy ' + srcdir + '\\' + self.outdir + 'boot.img ' + dstdir
                cmd_cpdtbo = 'copy ' + srcdir + '\\' + self.outdir + 'dtbo.img ' + dstdir
                os.popen(cmd_cpboot)
                os.popen(cmd_cpdtbo)

                finfo = open(dstdir + '\\' + self.notify_file, 'w+')
                finfo.write(info)
                finfo.close()
                open(taskpath + self.notifyflag_file, 'w+').close()
                self.notify(dstdir)

    def notify(self, dstdir):
            notify_file = dstdir + '\\' + self.notify_file
            os.popen('notepad ' + notify_file)

class DownloadTasks(Tasks):
    def __init__(self, mornitorpoint):
        super().__init__('downloadtasks', 'dl_', mornitorpoint)

    # def list_task(self):
    #     print('list_task', self.location)
    # 
    # def check_task(self):
    #     print('check_task', self.location)

    def handler(self, taskpath):
        self.notify(taskpath)

    def notify(self, taskpath):
        print('download ' + taskpath + ' complete')

class Monitor:
    def __init__(self, mornitorpoint):
        self.mornitorpoint = mornitorpoint
        self.taskset = []
        self.taskset.append(TimerTasks(self.mornitorpoint))
        self.taskset.append(BuildTasks(self.mornitorpoint))
        self.taskset.append(DownloadTasks(self.mornitorpoint))

    def run(self):
        for tasks in self.taskset:
            # 列出所有初始子任务集
            tasks.list_task()

        while True:
            time.sleep(3)
            #遍历任务集
            for tasks in self.taskset:
                #子任务集注册新任务
                tasks.register_new_task()

                #子任务集中任务检查
                tasks.check_task()

#test pass
mMonitor = Monitor('G:\Workspaces\python\prjs\dir\mornitorpoint\\')
mMonitor.run()

