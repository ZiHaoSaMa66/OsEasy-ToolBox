# import hmac
import os, time
from datetime import datetime
# from tkinter.messagebox import *
import pygetwindow as gw
import webbrowser
import ctypes
import sys
import psutil
import pyautogui
import socket
import re
import json

# import wmi
# from mainv3 import Ui



bkppath = "C:\\Backups"

cmdpath = "C:\\Users\\Administrator\\prod"


RunBoxKiller = False

RunProtectCMD = False

MMPCServRun = True

os.makedirs(cmdpath,mode=0o777,exist_ok=True)
os.makedirs(bkppath,mode=0o777,exist_ok=True)

class ToolBoxConfig:
    
    def __init__(self):
        
        self.config_file_path = "C:\\ToolBoxConfig.json"
        self.running_student_client_ver = 0
        self.oseasypath_have_been_modified = False
        self.studentExeName = "Student.exe"
        self.oseasypath = "C:\\Program Files (x86)\\Os-Easy\\os-easy multicast teaching system\\"
        
        pass
    
    def write_first_launch_time(self) -> None:
        '''写入首次启动时间'''
        reads = self.get_config_key_data("first_launch_time")
        if not reads:
            self.set_config_key_data("first_launch_time",get_time_str())
        
    
    def read_config(self) -> str:
        '''从配置文件中读取'''
        if checkPointFileIsExcs(self.config_file_path):
            with open(self.config_file_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            self.write_config("{}")
            return "{}"
    
    def write_config(self,datas:str | dict) -> None:
        '''写入配置文件'''
        
        if isinstance(datas,dict):
            datas = json.dumps(datas,ensure_ascii=False,indent=4)
        
        with open(self.config_file_path, "w", encoding="utf-8") as f:
            f.write(datas)
    
    
    def get_config_key_data(self,key) -> str | None:
        '''获取配置文件中指定键的数据'''
        return self.get_style_path(key)
    
    def set_config_key_data(self,key,value) -> None:
        '''设置配置文件中的数据'''
        self.set_style_path(key,value)
    
    def clear_config_key_data(self,key) -> None:
        '''清空配置文件中的数据'''
        cfg = self.read_config()
        if cfg == "{}":
            return
        jData:dict = json.loads(cfg)
        if key in jData:
            jData.pop(key)
        self.write_config(jData)
    
    
    def get_style_path(self,style_name:str) -> str | None:
        '''获取自定义外观的路径\n
        style_name: ["yiyan","fort","bg"]\n
        一言, 字体, 背景'''
        
        cfg = self.read_config()
        if cfg == "{}":
            return None
        jData = json.loads(cfg)
        if style_name in jData:
            return jData[style_name]
        return None
        
    
    def set_style_path(self,style_name:str,style_path:str) -> None:
        '''设置自定义外观的路径\n
        style_name: ["yiyan","fort","bg"]\n
        一言, 字体, 背景'''
        
        cfg = self.read_config()
        jData = json.loads(cfg)
        jData[style_name] = style_path
        self.write_config(jData)
        

Ui_Class = None

def pass_ui_class(ui:classmethod) -> None:
    '''传递Ui类到此处让这里的函数可以调用主Ui的函数'''
    global Ui_Class
    Ui_Class = ui

def TryGetStudentPath() -> tuple[str,str] | tuple[bool,None]:
    '''尝试获取学生端路径 并更新全局变量'''
    # global oseasypath,oseasypath_have_been_modified,studentExeName
    Spath = get_program_path("Student.exe")
    Spath_2 = get_program_path("MmcStudent.exe")
    # v10.9.1 学生端改名为MmcStudent.exe
    
    if Spath == None and Spath_2 == None:
        print("[DEBUG] > 未找到运行中的学生端")
        
        
        isModed = ToolBoxConfig().get_config_key_data("studentPath_have_been_modified")
        print(f"[DEBUG] 配置文件 > 学生端路径是否被修改：{isModed}")
        if not isModed:
            return False,None
        
        ToolBoxConfig().oseasypath_have_been_modified = True
        
        ToolBoxConfig().oseasypath = ToolBoxConfig().get_config_key_data("studentPath")
        ToolBoxConfig().studentExeName = ToolBoxConfig().get_config_key_data("studentExeName")
        
        print(f"[DEBUG] 配置文件 > 学生端路径为：{ToolBoxConfig().oseasypath}")
        print(f"[DEBUG] 配置文件 > 学生端进程名为：{ToolBoxConfig().studentExeName}")
        
        ToolBoxConfig().set_config_key_data("studentPath",ToolBoxConfig().oseasypath)
        ToolBoxConfig().set_config_key_data("studentExeName",ToolBoxConfig().studentExeName)
        
        
        
        return ToolBoxConfig().oseasypath,ToolBoxConfig().studentExeName


    if Spath_2:
        ToolBoxConfig().studentExeName = "MmcStudent.exe"
        Spath = Spath_2
    elif Spath:
        ToolBoxConfig().studentExeName = "Student.exe"
    
    Spath = str(Spath).replace("/","\\").replace("MmcStudent.exe","").replace("Student.exe","")
    ToolBoxConfig().oseasypath_have_been_modified = True
    ToolBoxConfig().oseasypath = Spath
    
    print(f"[DEBUG] 学生端路径为：{ToolBoxConfig().oseasypath}")
    print(f"[DEBUG] 学生端进程名为：{ToolBoxConfig().studentExeName}")
    
    ToolBoxConfig().set_config_key_data("studentPath",ToolBoxConfig().oseasypath)
    ToolBoxConfig().set_config_key_data("studentExeName",ToolBoxConfig().studentExeName)
    ToolBoxConfig().set_config_key_data("studentPath_have_been_modified",True)
    
    return ToolBoxConfig().oseasypath,ToolBoxConfig().studentExeName
    
    
def get_program_path(program_name) -> str | None:
    """
    获取指定程序的运行路径
    
    :param program_name: 程序名称，如 'exp.exe'
    
    :return: 程序的运行路径
    
    """
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['name'] == program_name:
                return proc.info['exe']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None





def usb_unlock():
    '''尝试解锁USB管控'''
    # 经过了好一段时间的研究可能真的就这样?
    summon_unlocknet()
    summon_unlock_usb()
    runbat('net.bat')
    time.sleep(2)
    runbat("usb.bat")
    # time.sleep(2)
    # runcmd("sc delete easyusbflt")
    # time.sleep(1)
    

def tryGuessStudentClientVer() -> int:
    '''尝试通过检测LissHeler.exe此类旧版本没有的程序\n
    来猜测学生端版本'''
    
    
    if not ToolBoxConfig().oseasypath_have_been_modified:
        _,_2 = TryGetStudentPath()
    
    

    versions = {
        109: f"{ToolBoxConfig().oseasypath}LissHelper.exe",
        108: f"{ToolBoxConfig().oseasypath}MultiClient.exe",
        105: f"{ToolBoxConfig().oseasypath}MouseKeyBoradControl.exe"
    }

    for version, path in versions.items():
        if checkPointFileIsExcs(path):
            print(f"[Student Ver Guess] maybe is v{version // 10}.{version % 10}")
            ToolBoxConfig().running_student_client_ver = version
            ToolBoxConfig().set_config_key_data("studentClientVer",version)
            return ToolBoxConfig().running_student_client_ver

    print("[Student Ver Guess] 超出检测范围 学生端本体可能损坏或路径不正确")
    ToolBoxConfig().running_student_client_ver = 0
    return ToolBoxConfig().running_student_client_ver
    
    pass

def HighVer_CloseMMPCProtectHelper():
    '''检查学生端版本来决定\n
    需不需要关闭MMPC保护服务\n
    '''
    if not ToolBoxConfig().running_student_client_ver:
       _ = tryGuessStudentClientVer()
    
    if ToolBoxConfig().running_student_client_ver >= 109:
        mpStatus = check_MMPC_status()
        if mpStatus:
            runcmd("sc stop MMPC")
            time.sleep(1)

    pass

def HighVer_AddCloseMMPC_CommandLine():
    '''检查学生端版本来决定\n
    需不需要向脚本追加关闭MMPC保护服务的命令\n
    '''
    
    if not ToolBoxConfig().running_student_client_ver:
       _ = tryGuessStudentClientVer()
       
    if ToolBoxConfig().running_student_client_ver >= 109:
        return "sc stop MMPC\n"
    return ""


def checkPointFileIsExcs(filePath) -> bool:
    '''检查文件是否存在'''
    return os.path.isfile(filePath)


def replace_ScreenRender() -> bool:
    '''替换原有scr用于拦截远程命令'''
    global bkppath
    filename = "ScreenRender_Helper.exe"
    nowcurhelper = os.path.join(os.getcwd(), filename)
    copypath = os.path.join(ToolBoxConfig().oseasypath, filename)

    onetime_protectcheck()
    if not checkPointFileIsExcs(nowcurhelper):
        return False

    runcmd(f'rename "{ToolBoxConfig().oseasypath}ScreenRender.exe" "ScreenRender_Y.exe"')
    time.sleep(2.5)
    runcmd(f'copy "{nowcurhelper}" "{copypath}"')
    time.sleep(2.5)
    runcmd(f'rename "{ToolBoxConfig().oseasypath}ScreenRender_Helper.exe" "ScreenRender.exe"')
    return True




def restone_ScreenRender() -> bool:
    '''还原原有的ScreenRender'''
    
    onetime_protectcheck()
    path = f"{ToolBoxConfig().oseasypath}ScreenRender.exe"
    
    a = check_tihuan_SCRY_status()
    if a==False:
        return False

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    runcmd(f'rename "{ToolBoxConfig().oseasypath}ScreenRender_Y.exe" "ScreenRender.exe"')

    return True


def get_yuancheng_cmd() -> str | None:
    '''从文件中读取拦截到的远程命令\n
    未读取到返回None'''
    getpath = os.path.join(cmdpath, "SCCMD.txt")
    try:
        with open(getpath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

# "C:\Program Files (x86)\Os-Easy\os-easy multicast teaching system\ScreenRender.exe" {#decoderName#:#h264#,#fullscreen#:0,#local#:#172.18.36.132#,#port#:7778,#remote#:#229.1.36.200#,#teacher_ip#:0,#verityPort#:7788}

def get_ipv4_address() -> str | None:
    '''获取机器IPv4地址'''
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        print(f"获取IPv4地址时出现错误: {e}")
        return None

def handin_save_yc_cmd(save_cmd) -> None:
    '''手动保存拦截的命令'''
    global cmdpath
    localIp = get_ipv4_address()
    save_cmd = re.sub(r"(#local#:)(#.*?#)", rf"\1#{localIp}#", save_cmd)
    getpath = os.path.join(cmdpath, "SCCMD.txt")
    
    with open(getpath, "w") as f:
        f.write(save_cmd)

def build_run_srcmd(YC_command) -> str:
    '''构造执行显示命令'''
    
    status = check_tihuan_SCRY_status()
    if status==True:
        fdb = f'"{ToolBoxConfig().oseasypath}ScreenRender_Y.exe" {YC_command}'
        return fdb
    else:
        fdb = f'"{ToolBoxConfig().oseasypath}ScreenRender.exe" {YC_command}'
        return fdb

def save_now_yccmd() -> bool | None:
    '''开发者选项 - 保存现在获取到的远程指令到程序目录'''
    getpath = cmdpath + "\\SCCMD.txt"
    savepath = os.getcwd() + "\\" + "command.txt"
    
    try:
        fm = open(getpath,'r')
        cmd = fm.read()
        fm.close()
    except FileNotFoundError:
        return None

    fm = open(savepath,'w')
    fm.write(cmd)
    fm.close()
    return True

def check_tihuan_SCRY_status() -> bool:
    '''通过检查SCR_Y是否存在
    \n来检查是否已经完成替换拦截程序
    \n返回True/False'''
    check_path = f"{ToolBoxConfig().oseasypath}ScreenRender_Y.exe"
    # try:
    #     fm = open(check_path,'r')
    #     fm.close()
    #     return True
    # except FileNotFoundError:
    #     return False
    
    return checkPointFileIsExcs(check_path)
    


def get_pid(name) -> int | None:
    '''
    根据进程名获取进程pid\n
    未寻找到返回None
    '''
    pids = psutil.process_iter()
    print("[" + name + "]'s pid is:")
    for pid in pids:
        if(pid.name() == name):
            print(pid.pid)
            return pid.pid
    return None

def get_time_str() -> str:
    '''返回一个时间字符串'''
    time_str = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return time_str


def get_scshot() -> None:
    '''保存一张屏幕截图'''

    savepath = os.getcwd()

    PMsize = pyautogui.size()
    print("DEBUG 屏幕尺寸 > ",PMsize)
    win_h = PMsize.height
    win_w = PMsize.width

    img = pyautogui.screenshot()

    mix_name = savepath + "\\" + get_time_str() + ".jpg"
    img.save(mix_name)
    print("DEBUG SavePath > ",mix_name)






def check_MMPC_status() -> bool:
    '''检查MMPC根服务状态\n
    返回True/False'''
    name = "MMPC"
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:

        return False

    if service and service['status'] == 'running':
        return True
    else:
        return False




def run_upto_admin() -> None:
    '''用于在非管理员运行时尝试提权'''
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"".join(sys.argv),None,1)
        sys.exit()

def del_historyrem(*e) -> None:
    '''删除保存的历史路径文件'''
    neddel = ['fontPath','bgPath','yiyanPath']
    
    for i in neddel:
        ToolBoxConfig().set_config_key_data(i,None)
    
    

def guaqi_process(process_name) -> str | bool:
    '''挂起进程'''
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                psutil.Process(pid).suspend()
                print(f"Process {process_name} (PID {pid}) suspended.")
                return True

        print(f"Process {process_name} not found.")
        return "尝试挂起的进程未找到"
    except psutil.AccessDenied as e:
        print(f"Permission error: {e}")
        return "尝试挂起进程失败"

def huifu_process(process_name) -> str | bool:
    '''恢复挂起进程'''
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                pid = process.info['pid']
                psutil.Process(pid).resume()
                print(f"Process {process_name} (PID {pid}) resumed.")
                return True

        print(f"Process {process_name} not found.")
        return "尝试恢复挂起的进程未找到"
    except psutil.AccessDenied as e:
        print(f"Permission error: {e}")
        return "尝试恢复挂起进程失败"



def onetime_protectcheck() -> None:
    '''检测是否开启了击杀脚本\n
    若未开启则帮助启动一次\n
    已经开启则忽略'''
    try:
        window = gw.getWindowsWithTitle('OsEasyToolBoxKiller')[0]
    except:
        summon_killer()
        runbat("k.bat")

def opengithubres(*e) -> None:
    '''在浏览器打开github仓库页面'''
    webbrowser.open("https://github.com/ZiHaoSaMa66/OsEasy-ToolBox")




def startprotect() -> None:
    global RunProtectCMD
    '''启动守护进程'''
    ptct = 0
    while RunProtectCMD==True:
        try:
            window = gw.getWindowsWithTitle('OsEasyToolBoxKiller')[0]
            time.sleep(0.5)
        except:
            runbat("k.bat")
            ptct += 1
            time.sleep(1)



def delcmdfiles() -> None:
    '''删除生成的脚本文件'''
    global cmdpath
    for filename in ["k.bat", "d.bat", "temp.bat", "kv2.bat", 'net.bat', 'usb.bat']:
        try:
            os.remove(os.path.join(cmdpath, filename))
        except FileNotFoundError:
            continue

def check_firsttime_start() -> bool:
    '''检查是否为第一次启动'''
    #用于第一次判断是否使用autodesk fix
    try:
        fm = open("C:\\FST.data","r")
        fm.close()
        return False
    except FileNotFoundError:
        fm = open("C:\\FST.data","w")
        fm.close()
        return True


def summon_unlocknet() -> None:
    '''生成解锁网络锁定脚本'''
    global cmdpath
    mp = cmdpath + "\\net.bat"
    fm = open(mp,"w")
    cmdtext = f"""@ECHO OFF\n
    title OsEasyToolBoxUnlockNetHeler\n
    {HighVer_AddCloseMMPC_CommandLine()}
    :a\n
    taskkill /f /t /im {ToolBoxConfig().studentExeName}\n
    taskkill /f /t /im DeviceControl_x64.exe\n
    goto a
    """
    fm.write(cmdtext)
    fm.close()

def summon_unlock_usb() -> None:
    '''生成解锁USB脚本'''
    global cmdpath
    mp = cmdpath + "\\usb.bat"
    fm = open(mp,"w")
    cmdtext = """@ECHO OFF\n
    title OsEasyToolBoxUnlockUSBHeler\n

    sc delete easyusbflt\n
    sc delete easyusbflt\n
    timeout 1\n
    
    del C:\\Windows\\System32\\drivers\\easyusbflt.sys\n
    timeout 5\n
    shutdown /l\n
    """
    fm.write(cmdtext)
    fm.close()



def summon_killerV2() -> None:
    '''生成V2击杀脚本'''
    global cmdpath
    mp = cmdpath + "\\kv2.bat"
    fm = open(mp,"w")
    cmdtext = f"@ECHO OFF\ntitle OsEasyToolBoxKillerV2\n:awa\nfor %%p in (Ctsc_Multi.exe,DeviceControl_x64.exe,HRMon.exe,MultiClient.exe,OActiveII-Client.exe,OEClient.exe,OELogSystem.exe,OEUpdate.exe,OEProtect.exe,ProcessProtect.exe,RunClient.exe,RunClient.exe,ServerOSS.exe,{ToolBoxConfig().studentExeName},wfilesvr.exe,tvnserver.exe,updatefilesvr.exe,ScreenRender.exe) do taskkill /f /IM %%p\ngoto awa\n"
    fm.write(cmdtext)
    fm.close()

def summon_killer() -> None:
    '''生成击杀脚本'''
    global cmdpath
    mp = cmdpath + "\\k.bat"
    fm = open(mp,"w")
    cmdtext = f"""@ECHO OFF\n
    title OsEasyToolBoxKiller\n
    
    {HighVer_AddCloseMMPC_CommandLine()}
    
    taskkill /f /t /im MultiClient.exe\n
    taskkill /f /t /im MultiClient.exe\n
    taskkill /f /t /im BlackSlient.exe\n
    :a\n
    taskkill /f /t /im {ToolBoxConfig().studentExeName}\n
    goto a"""
    fm.write(cmdtext)
    fm.close()

def backupOeKeyDll() -> None:
    '''备份OE的关键文件'''
    global bkppath
    print("[INFO] 尝试备份关键文件")
    namelist = ["oenetlimitx64.cat","OeNetLimitSetup.exe","OeNetLimit.sys","OeNetLimit.inf","MultiClient.exe","MultiClient.exe","LoadDriver.exe","BlackSlient.exe"]
    for filename in namelist:
        
        oepath = ToolBoxConfig().oseasypath + filename
        
        needbkpath =  bkppath + "\\" + filename

        runcmd(f'copy "{oepath}" "{needbkpath}"')

def restoneBlackSlt(*e) -> None:
    '''恢复黑屏安静程序'''
    global bkppath
    filename = "BlackSlient.exe"
    oepath = ToolBoxConfig().oseasypath + filename
    needbkpath =  bkppath + "\\" + filename
    runcmd(f'copy "{needbkpath}" "{oepath}"')

def restoneMutClient() -> None:
    '''恢复用于控屏的MultiClient'''
    global bkppath
    filename = "MultiClient.exe"
    oepath = ToolBoxConfig().oseasypath + filename
    needbkpath =  bkppath + "\\" + filename
    runcmd(f'copy "{needbkpath}" "{oepath}"')

def restoneKeyDll() -> None:
    '''恢复OE关键文件'''
    global bkppath
    print("尝试还原关键文件")
    namelist = ["oenetlimitx64.cat","OeNetLimitSetup.exe","OeNetLimit.sys","OeNetLimit.inf","MultiClient.exe","LoadDriver.exe","BlackSlient.exe"]
    for filename in namelist:
        oepath = ToolBoxConfig().oseasypath + filename
        needbkpath =  bkppath + "\\" + filename

        runcmd(f'copy "{needbkpath}" "{oepath}"')
    pass

def runbat(batname: str) -> None:
    '''运行指定名称的bat脚本'''
    global cmdpath
    batp = os.path.join(cmdpath, batname)
    os.startfile(batp)

def summon_deldll(delMtc:bool,shutdown:bool) -> None:
    '''生成删除dll脚本'''
    global cmdpath
    backupOeKeyDll()
    
    mp = cmdpath + "\\d.bat"
    fm = open(mp,"w")
    cmdtext = f"@ECHO OFF\ntitle OsEasyToolBox-Helper\ncd /D {ToolBoxConfig().oseasypath}\ntimeout 1\ndel /F /S OeNetLimitSetup.exe\ndel /F /S OeNetLimit.sys\ndel /F /S OeNetLimit.inf\ndel /F /S LockKeyboard.dll\ndel /F /S LoadDriver.exe\ndel /F /S LoadDriver.exe\ndel /F /S oenetlimitx64.cat\ndel /F /S BlackSlient.exe"
    if delMtc ==True:
        cmdtext += "\ndel /F /S MultiClient.exe"
    if shutdown ==False:
        pass
    elif shutdown ==True:
        cmdtext += "\ntimeout 5\nshutdown /l"
    #cmdtext += "\ntimeout 10\nshutdown /l"
    cmdtext += "\nexit"
    fm.write(cmdtext)
    fm.close()

def regkillercmd() -> None:
    '''生成击杀脚本并绑定粘滞键'''
    summon_killer()
    # mp = cmdpath + "\\r.bat"
    # fm = open(mp,"w")
    # cmdtext = 'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "C:\\Program Files\\dotnet\\k.bat"'
    # fm.write(cmdtext)
    # fm.close()
    # os.system("start C:\\Program Files\\dotnet\\r.bat")
    runcmd(f'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "{cmdpath}\\k.bat"')

def regkillerV2cmd() -> None:
    '''生成击杀脚本V2并绑定粘滞键'''
    summon_killerV2()
    runcmd(f'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "{cmdpath}\\kv2.bat"')

    
def boxkiller() -> None:
    global RunBoxKiller
    while RunBoxKiller==True:
    # os.system(command="taskkill /f /t /im Student.exe")
        opt = os.system(f"taskkill /f /t /im {ToolBoxConfig().studentExeName}")
        #print("test run")
        time.sleep(0.2)
    #print(f"[DEBUG] Killer Runned {opt}")

def runcmd(givecmd:str,*quiterun:bool) -> None:
    '''运行指定的命令'''
    if not quiterun:
        os.popen(cmd=givecmd)
    elif quiterun==False:
        os.system(command=givecmd)
    elif quiterun==True:
        os.popen(cmd=givecmd)
    else:
        os.system(command=givecmd)

def usecmd_runcmd(cmd:str) -> None:
    '''生成一个临时cmd文件运行指定命令'''
    global cmdpath
    mp = cmdpath + "\\temp.bat"
    fm = open(mp,"w")
    cmdtext = "@ECHO OFF\n"
    cmdtext += cmd
    cmdtext += "\nexit"
    fm.write(cmdtext)
    fm.close()
    runcmd(f"start {mp}")


def delSummonCmdFile(*e) -> None:
    #清理生成的脚本文件
    delcmdfiles()
def selfunc_g1(*e) -> None:
    #注册粘滞键替换击杀脚本
    regkillercmd()
    
def selfunc_g1plus(*e) -> None:
    #注册V2版本的替换击杀脚本
        regkillerV2cmd()

        
def delLockExeAndLogout(need_shutdown:bool) -> None:
    # showwarning("温馨提醒","此功能略微需要手速\n在工具箱帮助你注销以后\n只要看见可以重新登录后即可点出粘滞键的脚本完成解锁")
    # showwarning("温馨提醒","在注销后若无效果请手动重启机器\n(如果你的机房电脑有重启立刻还原请无视)\n(可以再次打开工具箱再次尝试注销解锁)\n并在进入系统桌面前手动点开粘滞键的击杀脚本\n若不想要注销可手动X掉命令窗口!!")
    summon_killer()
    onetime_protectcheck()
    summon_deldll(delMtc=True,shutdown=need_shutdown)
    time.sleep(2)
    runbat("d.bat")
    
def handToStartStudent(*e) -> None:

    usecmd_runcmd(f'"{ToolBoxConfig().oseasypath}{ToolBoxConfig().studentExeName}"')

# def selfunc_g5(*e):
#     restoneKeyDll()

def killerCmdProtect(*e) -> None:
    global RunProtectCMD
    if RunProtectCMD ==False:
        RunProtectCMD = True
        summon_killer()
        startprotect()
    elif RunProtectCMD ==True:
        RunProtectCMD = False
        usecmd_runcmd('taskkill /f /t /fi "imagename eq cmd.exe" /fi "windowtitle eq 管理员:  OsEasyToolBoxKiller"')

        

def unlockedNet() -> None:
    summon_unlocknet()
    runbat("net.bat")
    time.sleep(2)
    runcmd("sc stop OeNetlimit")
    time.sleep(1)
    usecmd_runcmd('taskkill /f /t /fi "imagename eq cmd.exe" /fi "windowtitle eq 管理员:  OsEasyToolBoxUnlockNetHeler"')
    time.sleep(1)

def startOsEasySelfToolBox(*e) -> None:
    # print("执行功能8 请稍等...")
    regkillercmd()
    onetime_protectcheck()
    time.sleep(2)
    runcmd(f'"{ToolBoxConfig().oseasypath}AssistHelper.exe"')