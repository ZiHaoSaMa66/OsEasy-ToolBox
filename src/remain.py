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

# import wmi
# from mainv3 import Ui



bkppath = "C:\\Backups"

cmdpath = "C:\\Users\\Administrator\\prod"

_loginpj = "C:\\Users\\Administrator\\temp\\rod\\"
loginpj = "C:\\Users\\Administrator\\temp\\rod\\passv2.txt"

oseasypath = "C:\\Program Files (x86)\\Os-Easy\\os-easy multicast teaching system\\"

oseasypath_have_been_modified = False

path_zidingyi_fort = "C:\\Users\\Administrator\\temp\\rod\\path_fort.txt"
path_zidingyi_bg = "C:\\Users\\Administrator\\temp\\rod\\path_bg.txt"
path_zidingyi_yiyan = "C:\\Users\\Administrator\\temp\\rod\\path_yiyan.txt"



running_student_client_ver = ""



RunBoxKiller = False

RunProtectCMD = False

MMPCServRun = True

os.makedirs(cmdpath,mode=0o777,exist_ok=True)
os.makedirs(bkppath,mode=0o777,exist_ok=True)
os.makedirs(_loginpj,mode=0o777,exist_ok=True)


def TryGetStudentPath():
    '''尝试获取学生端路径 并更新全局变量'''
    global oseasypath,oseasypath_have_been_modified
    Spath = get_program_path("Student.exe")
    if Spath == None:
        print("[DEBUG] > 未找到运行中的学生端")
        return False
    Spath = str(Spath).replace("/","\\").replace("Student.exe","")
    oseasypath_have_been_modified = True
    oseasypath = Spath
    print(f"[DEBUG] > 学生端路径为：{oseasypath}")
    return oseasypath
    
    
def get_program_path(program_name):
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

    
def getIfStudentPathHasModified():
    '''获取学生端路径是否被修改\n'''
    global oseasypath_have_been_modified
    return oseasypath_have_been_modified
    

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
    

def tryGuessStudentClientVer():
    '''尝试通过检测LissHeler.exe此类旧版本没有的程序\n
    来猜测学生端版本'''
    global oseasypath_have_been_modified,running_student_client_ver
    
    if not oseasypath_have_been_modified:
        _ = TryGetStudentPath()
        

    
    v10_9 = checkPointFileIsExcs(f"{oseasypath}LissHelper.exe")
    
    v10_8 = checkPointFileIsExcs(f"{oseasypath}MultiClient.exe")
    
    v10_5 = checkPointFileIsExcs(f"{oseasypath}MouseKeyBoradControl.exe")
    
    if v10_9:
        print("[Student Ver Guess] maybe is v10.9 ")
        running_student_client_ver = 109
    elif v10_8:
        print("[Student Ver Guess] maybe is v10.8 ")
        running_student_client_ver = 108
    elif v10_5:
        print("[Student Ver Guess] maybe is v10.5 ")
        running_student_client_ver = 105
    else:
        print("[Student Ver Guess] 超出检测范围 学生端本体可能损坏或路径不正确")
        running_student_client_ver = 0
    
    return running_student_client_ver
    
    pass

def HighVer_CloseMMPCProtectHelper():
    '''检查学生端版本来决定\n
    需不需要关闭MMPC保护服务\n
    '''
    if not running_student_client_ver:
       _ = tryGuessStudentClientVer()
    
    if running_student_client_ver >= 109:
        mpStatus = check_MMPC_status()
        if mpStatus:
            runcmd("sc stop MMPC")
            time.sleep(1)

    pass

def HighVer_AddCloseMMPC_CommandLine():
    '''检查学生端版本来决定\n
    需不需要向脚本追加关闭MMPC保护服务的命令\n
    '''
    global running_student_client_ver
    
    if not running_student_client_ver:
       _ = tryGuessStudentClientVer()
       
    if running_student_client_ver >= 109:
        return "sc stop MMPC\n"
    return ""



    

def checkPointFileIsExcs(filePath) -> bool:
    '''检查传入路径的指定文件是否存在\n
    返回True/False'''
    try:
        with open(filePath,'r') as f:
            pass
        return True
    except FileNotFoundError:
        return False
    except Exception as err:
        print(f"[ERR] 在检查 `{filePath}` 文件是否存在是被抛出异常{err}")
    pass


def replace_ScreenRender():
        '''替换原有scr用于拦截远程命令'''
        global bkppath,oseasypath
        filename = "ScreenRender_Helper.exe"
        # oepath = oseasypath + filename
        # needbkpath =  bkppath + "\\" + filename
        # runcmd(f'copy "{needbkpath}" "{oepath}"')
        nowrunpath = os.getcwd()
        nowcurhelper = nowrunpath + "\\" + filename
        
        copypath = oseasypath + filename
        
        # print("DEBUG > nowcurhelper",nowcurhelper)
        
        onetime_protectcheck()
        if not checkPointFileIsExcs(nowcurhelper):
            return False

        # print("执行重命名")
        runcmd(f'rename "{oseasypath}ScreenRender.exe" "ScreenRender_Y.exe"')
        time.sleep(2.5)
        # 将原有应用重命名
        # print("执行复制命令")
        # print(nowcurhelper)
        # print(copypath)
        runcmd(f'copy "{nowcurhelper}" "{copypath}"')
        # woc 哥们我真服了 双引号tmd漏一个
        time.sleep(2.5)
        # 复制拦截程序
        # print("拦截程序重命名")
        runcmd(f'rename "{oseasypath}ScreenRender_Helper.exe" "ScreenRender.exe"')
        #将拦截程序重命名
        return True




def restone_ScreenRender():
    '''还原原有的ScreenRender'''
    global oseasypath
    onetime_protectcheck()
    path = f"{oseasypath}ScreenRender.exe"
    check_path = "C:\Program Files (x86)\Os-Easy\os-easy multicast teaching system\ScreenRender_Y.exe"
    
    a = check_tihuan_SCRY_status()
    if a==False:
        return False

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    runcmd(f'rename "{oseasypath}ScreenRender_Y.exe" "ScreenRender.exe"')

    return True


def get_yuancheng_cmd():
    '''从文件中读取拦截到的远程命令\n
    未读取到返回None'''
    getpath = cmdpath + "\\SCCMD.txt"
    try:
        fm = open(getpath,'r')
        cmd = fm.read()
        fm.close()
        return cmd
    except FileNotFoundError:
        return None

# "C:\Program Files (x86)\Os-Easy\os-easy multicast teaching system\ScreenRender.exe" {#decoderName#:#h264#,#fullscreen#:0,#local#:#172.18.36.132#,#port#:7778,#remote#:#229.1.36.200#,#teacher_ip#:0,#verityPort#:7788}

def handin_save_yc_cmd(save_cmd):
    '''开发者选项 - 手动保存拦截的命令'''
    global cmdpath
    getpath = cmdpath + "\\SCCMD.txt"

    fm = open(getpath,"w")
    fm.write(str(save_cmd))
    fm.close()

def build_run_srcmd(YC_command):
    '''构造执行显示命令'''
    global oseasypath
    
    status = check_tihuan_SCRY_status()
    if status==True:
        fdb = f'"{oseasypath}ScreenRender_Y.exe" {YC_command}'
        return fdb
    else:
        fdb = f'"{oseasypath}ScreenRender.exe" {YC_command}'
        return fdb

def save_now_yccmd():
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

def check_tihuan_SCRY_status():
    '''通过检查SCR_Y是否存在
    \n来检查是否已经完成替换拦截程序
    \n返回True/False'''
    global oseasypath
    check_path = f"{oseasypath}ScreenRender_Y.exe"
    # try:
    #     fm = open(check_path,'r')
    #     fm.close()
    #     return True
    # except FileNotFoundError:
    #     return False
    
    return checkPointFileIsExcs(check_path)
    


def get_pid(name):
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

def get_time_str():
    '''返回一个时间字符串'''
    time_str = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return time_str


def get_scshot():
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






def check_MMPC_status():
    '''检查MMPC根服务状态\n
    返回True/False'''
    # f=os.popen("sc query MMPC")
    name = "MMPC"
# def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # print(str(ex))
        return False
    # return service

    if service and service['status'] == 'running':
        return True
    else:
        return False




def run_upto_admin():
    '''用于在非管理员运行时尝试提权'''
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"".join(sys.argv),None,1)
        sys.exit()

def del_historyrem(*e):
    '''删除保存的历史路径文件'''
    neddel = [path_zidingyi_bg,path_zidingyi_fort,path_zidingyi_yiyan]
    for name in neddel:
        try:
            os.remove(name)
        except FileNotFoundError:
            pass

# def suspend_process(process_name):
def guaqi_process(process_name):
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

# def resume_process(process_name):
def huifu_process(process_name):
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



def onetime_protectcheck():
    '''检测是否开启了击杀脚本\n
    若未开启则帮助启动一次\n
    已经开启则忽略'''
    try:
        window = gw.getWindowsWithTitle('OsEasyToolBoxKiller')[0]
    except:
        summon_killer()
        runbat("k.bat")

def opengithubres(*e):
    '''在浏览器打开github仓库页面'''
    webbrowser.open("https://github.com/ZiHaoSaMa66/OsEasy-ToolBox")




def startprotect():
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



def delcmdfiles():
    '''删除生成的脚本文件'''
    global cmdpath
    fln = ["k.bat","d.bat","temp.bat","kv2.bat",'net.bat','usb.bat']
    for i in fln:
        try:
            swpath = cmdpath + "\\" + i
            os.remove(swpath)
        except Exception:
            pass

def check_firsttime_start():
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

# os.makedirs(cmdpath,mode=0o777,exist_ok=True)
def summon_unlocknet():
    '''生成解锁网络锁定脚本'''
    global cmdpath
    mp = cmdpath + "\\net.bat"
    fm = open(mp,"w")
    cmdtext = f"""@ECHO OFF\n
    title OsEasyToolBoxUnlockNetHeler\n
    {HighVer_AddCloseMMPC_CommandLine()}
    :a\n
    taskkill /f /t /im Student.exe\n
    taskkill /f /t /im DeviceControl_x64.exe\n
    goto a
    """
    fm.write(cmdtext)
    fm.close()

def summon_unlock_usb():
    '''生成解锁USB脚本'''
    global cmdpath
    mp = cmdpath + "\\usb.bat"
    fm = open(mp,"w")
    cmdtext = """@ECHO OFF\n
    title OsEasyToolBoxUnlockUSBHeler\n

    sc delete easyusbflt\n
    sc delete easyusbflt\n
    timeout 1\n
    
    del C:\Windows\System32\drivers\easyusbflt.sys\n
    timeout 5\n
    shutdown /l\n
    """
    fm.write(cmdtext)
    fm.close()



def summon_killerV2():
    '''生成V2击杀脚本'''
    global cmdpath
    mp = cmdpath + "\\kv2.bat"
    fm = open(mp,"w")
    cmdtext = "@ECHO OFF\ntitle OsEasyToolBoxKillerV2\n:awa\nfor %%p in (Ctsc_Multi.exe,DeviceControl_x64.exe,HRMon.exe,MultiClient.exe,OActiveII-Client.exe,OEClient.exe,OELogSystem.exe,OEUpdate.exe,OEProtect.exe,ProcessProtect.exe,RunClient.exe,RunClient.exe,ServerOSS.exe,Student.exe,wfilesvr.exe,tvnserver.exe,updatefilesvr.exe,ScreenRender.exe) do taskkill /f /IM %%p\ngoto awa\n"
    fm.write(cmdtext)
    fm.close()

def summon_killer():
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
    taskkill /f /t /im Student.exe\n
    goto a"""
    fm.write(cmdtext)
    fm.close()

def backupOeKeyDll():
    '''备份OE的关键文件'''
    global bkppath,oseasypath
    print("尝试备份关键文件")
    namelist = ["oenetlimitx64.cat","OeNetLimitSetup.exe","OeNetLimit.sys","OeNetLimit.inf","MultiClient.exe","MultiClient.exe","LoadDriver.exe","BlackSlient.exe"]
    for filename in namelist:
        oepath = oseasypath + filename
        needbkpath =  bkppath + "\\" + filename

        # print("oepath>>",oepath)
        # print("nedbkpath>>",needbkpath)
        # runcmd()
        # runcmd(f'copy "{oepath}" "{needbkpath}"\npause')
        runcmd(f'copy "{oepath}" "{needbkpath}"')

def restoneBlackSlt(*e):
    '''恢复黑屏安静程序'''
    global bkppath,oseasypath
    filename = "BlackSlient.exe"
    oepath = oseasypath + filename
    needbkpath =  bkppath + "\\" + filename
    runcmd(f'copy "{needbkpath}" "{oepath}"')

def restoneMutClient():
    '''恢复用于控屏的MultiClient'''
    global bkppath,oseasypath
    filename = "MultiClient.exe"
    oepath = oseasypath + filename
    needbkpath =  bkppath + "\\" + filename
    runcmd(f'copy "{needbkpath}" "{oepath}"')

def restoneKeyDll():
    '''恢复OE关键文件'''
    global bkppath,oseasypath
    print("尝试还原关键文件")
    namelist = ["oenetlimitx64.cat","OeNetLimitSetup.exe","OeNetLimit.sys","OeNetLimit.inf","MultiClient.exe","LoadDriver.exe","BlackSlient.exe"]
    for filename in namelist:
        oepath = oseasypath + filename
        needbkpath =  bkppath + "\\" + filename

        runcmd(f'copy "{needbkpath}" "{oepath}"')
    pass

def runbat(batname:str):
    '''运行指定名称的bat脚本'''
    global cmdpath
    batp = cmdpath + "\\" + batname
    runcmd(f'start {batp}')

def summon_deldll(delMtc:bool,shutdown:bool):
    '''生成删除dll脚本'''
    global cmdpath,oseasypath
    backupOeKeyDll()
    
    mp = cmdpath + "\\d.bat"
    fm = open(mp,"w")
    cmdtext = f"@ECHO OFF\ntitle OsEasyToolBox-Helper\ncd /D {oseasypath}\ntimeout 1\ndel /F /S OeNetLimitSetup.exe\ndel /F /S OeNetLimit.sys\ndel /F /S OeNetLimit.inf\ndel /F /S LockKeyboard.dll\ndel /F /S LoadDriver.exe\ndel /F /S LoadDriver.exe\ndel /F /S oenetlimitx64.cat\ndel /F /S BlackSlient.exe"
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

def regkillercmd():
    '''生成击杀脚本并绑定粘滞键'''
    summon_killer()
    # mp = cmdpath + "\\r.bat"
    # fm = open(mp,"w")
    # cmdtext = 'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "C:\\Program Files\\dotnet\\k.bat"'
    # fm.write(cmdtext)
    # fm.close()
    # os.system("start C:\\Program Files\\dotnet\\r.bat")
    runcmd(f'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "{cmdpath}\\k.bat"')

def regkillerV2cmd():
    '''生成击杀脚本V2并绑定粘滞键'''
    summon_killerV2()
    runcmd(f'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe" /v Debugger /t REG_SZ /d "{cmdpath}\\kv2.bat"')

    
def boxkiller():
    global RunBoxKiller
    while RunBoxKiller==True:
    # os.system(command="taskkill /f /t /im Student.exe")
        opt = os.system("taskkill /f /t /im Student.exe")
        #print("test run")
        time.sleep(0.2)
    #print(f"[DEBUG] Killer Runned {opt}")

def runcmd(givecmd:str,*quiterun:bool):
    '''运行指定的命令'''
    if not quiterun:
        os.popen(cmd=givecmd)
    elif quiterun==False:
        os.system(command=givecmd)
    elif quiterun==True:
        os.popen(cmd=givecmd)
    else:
        os.system(command=givecmd)

def usecmd_runcmd(cmd:str):
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


def selfunc_g0(*e):
    #清理生成的脚本文件
    delcmdfiles()
def selfunc_g1(*e):
    #注册粘滞键替换击杀脚本
    regkillercmd()
    
def selfunc_g1plus(*e):
    #注册V2版本的替换击杀脚本
        regkillerV2cmd()

def selfunc_g2(*e):
    global RunBoxKiller
    # result = askquestion("温馨提示","此功能为半成品功能\n是否继续?")
    # # print(result)
    # if result =="yes":
    if RunBoxKiller ==False:
        # save_loginwithoutpwd()
        RunBoxKiller = True
        boxkiller()
    elif RunBoxKiller ==True:
        RunBoxKiller = False
        
def selfunc_g3(need_shutdown:bool):
    # showwarning("温馨提醒","此功能略微需要手速\n在工具箱帮助你注销以后\n只要看见可以重新登录后即可点出粘滞键的脚本完成解锁")
    # showwarning("温馨提醒","在注销后若无效果请手动重启机器\n(如果你的机房电脑有重启立刻还原请无视)\n(可以再次打开工具箱再次尝试注销解锁)\n并在进入系统桌面前手动点开粘滞键的击杀脚本\n若不想要注销可手动X掉命令窗口!!")
    summon_killer()
    onetime_protectcheck()
    summon_deldll(delMtc=True,shutdown=need_shutdown)
    time.sleep(2)
    runbat("d.bat")
    
def selfunc_g4(*e):
    global oseasypath
    usecmd_runcmd(f'"{oseasypath}Student.exe"')

def selfunc_g5(*e):
    restoneKeyDll()

def selfunc_g6(*e):
    global RunProtectCMD
    if RunProtectCMD ==False:
        RunProtectCMD = True
        summon_killer()
        startprotect()
    elif RunProtectCMD ==True:
        RunProtectCMD = False
        usecmd_runcmd('taskkill /f /t /fi "imagename eq cmd.exe" /fi "windowtitle eq 管理员:  OsEasyToolBoxKiller"')

        

def selfunc_g7():
    summon_unlocknet()
    runbat("net.bat")
    time.sleep(2)
    runcmd("sc stop OeNetlimit")
    time.sleep(1)
    usecmd_runcmd('taskkill /f /t /fi "imagename eq cmd.exe" /fi "windowtitle eq 管理员:  OsEasyToolBoxUnlockNetHeler"')
    time.sleep(1)

def selfunc_g8(*e):
    # print("执行功能8 请稍等...")
    regkillercmd()
    onetime_protectcheck()
    time.sleep(2)
    runcmd(f'"{oseasypath}AssistHelper.exe"')