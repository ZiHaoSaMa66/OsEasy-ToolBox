from remain import *

run_upto_admin()


fstst = ToolBoxCfg.first_launch_check()
if fstst == True:
    usecmd_runcmd(
        'rename "C:\\Program Files\\Autodesk\\Autodesk Sync\\AdSyncNamespace.dll" "AdSyncNamespace.dll.bak"'
    )
# fixed pyqt bind to autodesk360 dll

import flet as ft

# 0.18.0

import random

from pynput import keyboard


fontpath = "C:\\Windows\\Fonts\\simhei.ttf"


class Ui:

    def __init__(self) -> None:

        self.ver = "OsEasy-ToolBox v1.7 Beta3.1"

        self.runwindows_lis = keyboard.Listener(on_press=self.run_windowskjj_onpress)

        # 构造监听器对象listener
        self.JieTu_listener = keyboard.Listener(on_press=self.JT_on_press)

        self.RunFullSC_listener = keyboard.Listener(on_press=self.FullSC_on_press)

        self.KillSCR_listener = keyboard.Listener(on_press=self.SCR_on_press)

        self.runwindows_press_alt = False
        self.runwindows_press_u = False

        self.SCR_Press_K = False
        self.SCR_Press_Alt = False

        self.Press_X = False
        self.Press_Alt = False

        self.guaqi_runstatus = False  # 挂起进程状态
        self.bgtmd = 0.6  # 初始化 背景图片透明度值
        self.defult_yy = True  # 默认一言库
        self.font_loadtime = 1

        self.NowSelIndex = "0"  # 防止无变量的初始化

        self.yiyanshowtext = ft.Text("", size=16)
        self.yiyanshowtext2 = ft.Text("", size=16)

        self.loaded_bg = False

        pass

    def FullSC_on_press(self, key):
        """用于快捷键运行全屏控制窗口"""

        if str(key) == "<70>":
            if self.KillSCR_swc.value == False:
                self.show_snakemessage(
                    "警告！ 未开启快捷键杀广播进程\n尝试运行的操作已拦截...."
                )
            else:
                status = get_yuancheng_cmd()
                if status == None:
                    self.show_snakemessage("未拦截到控制命令参数")
                else:
                    cmd = status.replace("#fullscreen#:0", "#fullscreen#:1")
                    builded = build_run_srcmd(cmd)
                    runcmd(builded)
                    # Fix 黑框

    def dic_RunFullSC(self, *e):
        """按钮点击直接运行全屏广播指令"""
        status = get_yuancheng_cmd()

        if self.KillSCR_swc.value == True:

            if status == None:
                self.show_snakemessage("未拦截到控制命令参数")
            else:
                cmd = status.replace("#fullscreen#:0", "#fullscreen#:1")
                builded = build_run_srcmd(cmd)
                print("DEBUG with build cmd", builded)
                runcmd(builded)

        else:
            self.show_snakemessage(
                "警告！ 未开启快捷键杀广播进程\n尝试运行的操作已拦截...."
            )

    def SCR_on_press(self, key):
        """用于检测快捷键杀SCR_Y进程"""

        if key == keyboard.KeyCode(char="K") or key == keyboard.KeyCode(char="k"):
            self.SCR_Press_K = True
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            self.SCR_Press_Alt = True

        if self.SCR_Press_Alt and self.SCR_Press_K:
            self.SCR_Press_Alt = self.SCR_Press_K = False  # 重置按键按下状态
            # get_scshot()
            runcmd("taskkill /f /t /im ScreenRender_Y.exe")
            runcmd("taskkill /f /t /im ScreenRender.exe")

    def dic_KillSCR(self, *e):
        """点击按钮直接杀屏幕广播进程"""
        runcmd("taskkill /f /t /im ScreenRender_Y.exe")
        runcmd("taskkill /f /t /im ScreenRender.exe")

    def JT_on_press(self, key):
        """当监听器检测到键盘按下"""

        if key == keyboard.KeyCode(char="x") or key == keyboard.KeyCode(char="X"):
            self.Press_X = True
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            self.Press_Alt = True

        if self.Press_Alt and self.Press_X:
            self.Press_Alt = self.Press_X = False  # 重置按键按下状态
            get_scshot()

        pass

    def run_windowskjj_onpress(self, key):
        """快捷键触发运行窗口广播"""
        if key == keyboard.KeyCode(char="U") or key == keyboard.KeyCode(char="u"):
            self.runwindows_press_u = True
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            self.runwindows_press_alt = True

        if self.runwindows_press_alt and self.runwindows_press_u:
            self.runwindows_press_u = self.runwindows_press_alt = False

            self.Get_yccmd_loj("e")

        pass

    def theme_changed(self, *e):

        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.ztqhb.label = (
            "亮色主题" if self.page.theme_mode == ft.ThemeMode.LIGHT else "暗色主题"
        )
        self.page.update()

    def try_get_history_path(self):
        """尝试获取历史路径"""
        if fstst != True:
            bgPath = ToolBoxCfg.get_style_path("bgPath")
            if bgPath:
                self.bgpath = bgPath
                self.bgtmdb.disabled = False
                self.loaded_bg = True
                self.reflashbg()

            yiyanPath = ToolBoxCfg.get_style_path("yiyanPath")
            if yiyanPath:
                self.yiyanfpath = yiyanPath
                self.loadyiyan()

            fontPath = ToolBoxCfg.get_style_path("fontPath")
            if fontPath:
                self.zdy_fontpath = fontPath
                self.setup_zidingyi_font()

    def enable_usb(self):
        pass

    def close_askdel_dlg(self, xueze):
        self.unlock_func_askdlg.open = False
        self.page.update()
        if xueze == None:
            self.show_snakemessage("取消解锁了")
        else:
            delLockExeAndLogout(xueze)

    def open_askdel_dlg(self, *e):
        self.page.dialog = self.unlock_func_askdlg
        self.unlock_func_askdlg.open = True
        self.page.update()

    def close_col_readme_dlg(self):
        self.col_readme_dlg.open = False
        self.show_snakemessage("Have Fun")
        self.page.update()

    def open_col_readme_dlg(self, *e):
        self.page.dialog = self.col_readme_dlg
        self.col_readme_dlg.open = True
        self.page.update()

    def main(self, bruh: ft.Page):
        self.page = bruh
        self.page.title = self.ver
        self.page.fonts = {"ht": fontpath}
        self.page.theme = ft.Theme(font_family="ht")
        self.page.update()

        self.page.window_height = 615
        self.page.window_width = 450

        self.page.window_max_height = 2000
        self.page.window_max_width = 455

        self.page.window_min_height = 500
        self.page.window_min_width = 449

        self.page.window_min_height = 500
        self.page.window_min_width = 449

        self.page.update()

        self.unlock_func_askdlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("解锁选项"),
            content=ft.Text(
                "选择适合你的选项\n三者一起: 删除黑屏安静+解除键盘锁+删除控屏锁定程序 (需要注销)\n仅控屏: 仅删除控屏锁定程序"
            ),
            actions=[
                ft.TextButton(
                    "三者一起", on_click=lambda _: self.close_askdel_dlg(xueze=True)
                ),
                ft.TextButton(
                    "仅控屏锁定程序",
                    on_click=lambda _: self.close_askdel_dlg(xueze=False),
                ),
                ft.TextButton(
                    "取消", on_click=lambda _: self.close_askdel_dlg(xueze=None)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            # on_dismiss=lambda _:self.close_askdel_dlg(xueze=None),
        )

        self.col_readme_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("控屏管理页使用说明"),
            content=ft.Text(
                "在使用前请先使用解锁键盘锁&删除控制锁定软件功能\n点击替换拦截程序后再恢复控屏软件\n等待老师控制屏幕后即完成拦截远程命令\n完成替换后即可重新删除控屏软件\n此时当老师处于控制状态时你可以主动运行命令弹出窗口化共享屏幕\n实现自由的同时不影响听课!!\n当老师来时你可以使用快捷键启动全屏参数的控制\n等待老师走后再用快捷键清理进程"
            ),
            actions=[
                ft.TextButton("晓得了", on_click=lambda _: self.close_col_readme_dlg()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda _: self.close_col_readme_dlg(),
        )

        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)

        self.yiyan_pick_files_dialog = ft.FilePicker(
            on_result=self.yiyan_pick_files_result
        )

        self.font_pick_files_dialog = ft.FilePicker(
            on_result=self.font_pick_files_result
        )
        # selected_files = ft.Text()

        self.bgfilepick = ft.ElevatedButton(
            "切换背景图片",
            icon=ft.icons.UPLOAD_FILE,
            on_click=lambda _: self.pick_files_dialog.pick_files(
                allow_multiple=False, file_type="IMAGE"
            ),
        )
        # 切换背景图片按钮

        self.ztqhb = ft.Switch(
            label="亮色主题", on_change=self.theme_changed, value=True
        )
        # 切换主题开关
        self.bgtmd_text = ft.Text("滑动以调整背景图片不透明度")

        self.bgtmdb = ft.Slider(
            min=0.0,
            max=1.0,
            divisions=0.1,
            value=0.6,
            on_change_end=self.change_bg_btmd,
            disabled=True,
        )
        # 背景不透明度滑条
        self.yiyanbtn = ft.ElevatedButton(
            "加载外部一言文件",
            icon=ft.icons.UPLOAD_SHARP,
            on_click=lambda _: self.yiyan_pick_files_dialog.pick_files(
                allow_multiple=False, allowed_extensions=["txt"]
            ),
        )
        # 一言加载

        self.zitibtn = ft.ElevatedButton(
            "更换显示字体",
            icon=ft.icons.UPLOAD_SHARP,
            on_click=lambda _: self.font_pick_files_dialog.pick_files(
                allow_multiple=False, allowed_extensions=["ttf"]
            ),
        )
        # 自定义字体切换

        self.remove_rem = ft.ElevatedButton(
            "清除历史路径记忆", icon=ft.icons.DELETE_OUTLINE, on_click=del_historyrem
        )

        self.list_all_pickdialog = [
            self.pick_files_dialog,
            self.yiyan_pick_files_dialog,
            self.font_pick_files_dialog,
        ]
        # 选择文件对话框 需要在添加完组件后进行添加 不然无法进行选择文件

        self.guaqi_sw = ft.Switch(
            label="挂起学生端", active_color="pink", on_change=self.guaqi_chufa
        )

        self.mmpc_sw = ft.FilledTonalButton(
            text="长按开&关学生端根服务",
            icon=ft.icons.BACK_HAND_OUTLINED,
            on_long_press=self.MMPC_shutdown_start_chufa,
            on_hover=self.only_update_MMPC_status,
        )
        self.mmpc_Stext = ft.TextField(
            label="根服务状态",
            value="未知 (点我更新状态)",
            read_only=True,
            on_focus=self.only_update_MMPC_status,
            text_align=ft.TextAlign.CENTER,
        )
        # self.stud_pid = ft.TextField(label="学生端PID", disabled=True, value="未知")

        self.FastGetSC = ft.Switch(
            label="Alt+X 快捷键屏幕截图", on_change=self.HotKey_screenshot
        )

        # self.yiyanshowtext2,ft.Divider(),
        # self.yiyanshowtext2 = self.yiyanshowtext

        self.funcTab_Stuff = ft.Column(
            controls=[
                self.yiyanshowtext,
                ft.Divider(height=1),
                self.mmpc_Stext,
                self.mmpc_sw,
                ft.FilledTonalButton(
                    text="长按重启学生端",
                    icon=ft.icons.RESTORE,
                    on_long_press=handToStartStudent,
                ),
                ft.FilledTonalButton(
                    text="重新获取学生端路径",
                    icon=ft.icons.REFRESH,
                    on_click=self.reflashStudentPath,
                ),
                ft.FilledTonalButton(
                    text="注册粘滞键替换", icon=ft.icons.COPY_SHARP, on_click=selfunc_g1
                ),
                ft.Switch(
                    label="外部cmd守护进程",
                    active_color="green",
                    on_change=killerCmdProtect,
                ),
                self.guaqi_sw,
                ft.FilledTonalButton(
                    text="打开噢易自带工具",
                    icon=ft.icons.OPEN_IN_NEW,
                    on_click=startOsEasySelfToolBox,
                ),
            ]
        )

        self.func_SecondTab_Stuff = ft.Column(
            controls=[
                self.yiyanshowtext,
                ft.Divider(height=1),
                ft.FilledTonalButton(
                    text="长按以删除脚本文件",
                    icon=ft.icons.CLEANING_SERVICES_OUTLINED,
                    on_long_press=delSummonCmdFile,
                ),
                ft.FilledTonalButton(
                    text="删除键盘锁驱动&控屏锁定程序",
                    icon=ft.icons.KEYBOARD_SHARP,
                    on_click=self.open_askdel_dlg,
                ),
                ft.FilledTonalButton(
                    text="长按恢复所有备份文件",
                    icon=ft.icons.RESTORE,
                    on_long_press=lambda e: restoneKeyDll,
                ),
                ft.FilledTonalButton(
                    text="长按以恢复黑屏安静程序",
                    icon=ft.icons.ACCOUNT_BOX,
                    on_long_press=restoneBlackSlt,
                ),
                ft.FilledTonalButton(
                    text="长按以仅恢复控屏锁定程序",
                    icon=ft.icons.SCREEN_SHARE_SHARP,
                    on_long_press=restoneMutClient,
                ),
                ft.FilledTonalButton(
                    text="解除软件网络限制",
                    icon=ft.icons.WIFI_PASSWORD_SHARP,
                    on_click=self.forunlocknettips,
                ),
                ft.FilledTonalButton(
                    text="[BETA] 关闭USB管控服务",
                    icon=ft.icons.USB_SHARP,
                    on_click=self.usb_unlock_tips,
                ),
                self.FastGetSC,
            ]
        )

        self.teachIp_input = ft.TextField(label="输入教师端IP地址")
        # 自动生成命令
        self.auto_gennerate_cmd = ft.FilledTonalButton(
            text="自动生成远程命令",
            icon=ft.icons.CODE,
            on_click=lambda _: generate_yc_cmd_and_save(self.teachIp_input.value),
        )

        self.conl_save_ycCmd_input = ft.TextField(label="键入完整的远程广播命令")
        self.conl_ycCmd_update = ft.FilledTonalButton(
            "手动更新完整远程广播命令",
            on_click=lambda _: handin_save_yc_cmd(self.conl_save_ycCmd_input.value),
            icon=ft.icons.UPDATE,
        )

        self.conl_getyccmd_btn = ft.FilledTonalButton(
            text="读取已拦截的广播命令",
            icon=ft.icons.BOOK,
            on_click=self.dev_read_lj_cmd_loj,
        )

        self.col_readme_dig = ft.FilledButton(
            "点我查看此页面的使用说明", on_click=self.open_col_readme_dlg
        )

        self.RunFullSC_btn = ft.FilledTonalButton(
            "长按运行全屏广播命令",
            on_long_press=self.dic_RunFullSC,
            icon=ft.icons.FULLSCREEN,
        )

        self.restone_scr = ft.FilledTonalButton(
            text="恢复原有屏幕广播程序",
            on_click=self.restone_SCR_loj,
            icon=ft.icons.RESTORE_PAGE,
        )
        self.tihuan_scr = ft.FilledTonalButton(
            text="替换拦截命令程序",
            on_click=self.replace_SCR_loj,
            icon=ft.icons.FIND_REPLACE,
        )

        self.RunFullSC_swc = ft.Switch(
            label="Ctrl+Alt+F 以全屏运行广播命令",
            on_change=self.HotKey_RunFullSCR,
            active_color="pink",
        )

        self.KillSCR_btn = ft.FilledTonalButton(
            "手动杀屏幕广播进程",
            icon=ft.icons.BACK_HAND_OUTLINED,
            on_click=self.dic_KillSCR,
        )

        self.KillSCR_swc = ft.Switch(
            label="Alt+K 杀屏幕广播进程",
            on_change=self.HotKey_KillSCR,
            active_color="pink",
        )

        self.runwindows_swc = ft.Switch(
            label="Alt+U 运行窗口屏幕广播",
            on_change=self.hotkey_runwindows,
            active_color="pink",
        )

        self.try_read_sharecmd = ft.FilledTonalButton(
            text="运行窗口化广播命令",
            on_click=self.Get_yccmd_loj,
            icon=ft.icons.WINDOW_SHARP,
        )

        self.waiguanTab_Stuff = ft.Column(
            controls=[
                self.yiyanshowtext,
                ft.Divider(height=1),
                self.ztqhb,
                self.remove_rem,
                self.zitibtn,
                self.bgfilepick,
                self.bgtmd_text,
                self.bgtmdb,
                self.yiyanbtn,
            ]
        )

        self.MyRail = ft.NavigationRail(
            selected_index=0,
            label_type="ALL",
            min_width=30,
            min_extended_width=30,
            group_alignment=-0.8,
            expand=False,
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.AUTO_FIX_HIGH_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.AUTO_FIX_HIGH),
                    label="进程管理",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.INTEGRATION_INSTRUCTIONS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.INTEGRATION_INSTRUCTIONS),
                    label_content=ft.Text("其他管理"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SCREEN_SHARE_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SCREEN_SHARE_SHARP),
                    label_content=ft.Text("广播管理"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.STYLE_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.STYLE),
                    label_content=ft.Text("外观"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.FAVORITE_BORDER_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.FAVORITE, color="red"),
                    label="关于",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label="DevTools",
                ),
            ],
            on_change=lambda e: self.selPages_Helper(e.control.selected_index),
        )
        # on_change=lambda e: print("Selected destination:", e.control.selected_index)

        # self.base_mix = ft.Row(self.Rail , ft.VerticalDivider(width=1))
        self.pickrandomyiyan()

        self.SWC_MainPages_0()

        self.added_pickdialog()

        self.try_get_history_path()

        self.reflashStudentPath()

        pass_ui_class(self)

    def reflashStudentPath(self, *e):
        global oseasypath
        """重新获取学生端路径\n
        设计上的一点问题.. 干活的函数没办法直接弹窗\n
        只能用个写在UI类里多余的函数来做"""

        # status, studentName = TryGetStudentPath()
        _ = tryGuessStudentClientVer()
        # 没啥用只是顺带需要更新一下学生端版本

        if ToolBoxCfg.oseasypath_have_been_modified != False:
            self.show_snakemessage(
                f"更新学生端路径成功\n{ToolBoxCfg.oseasypath}\n学生端进程名:{ToolBoxCfg.studentExeName}"
            )
        else:
            self.show_snakemessage(f"更新路径失败\n也许是学生端未运行??")
        pass

    def HotKey_screenshot(self, *e):
        """快捷键截图开关触发函数"""

        if self.FastGetSC.value == True:

            self.JieTu_listener.run()

        elif self.FastGetSC.value == False:

            self.JieTu_listener.stop()
        pass

    def HotKey_RunFullSCR(self, *e):

        if self.RunFullSC_swc.value == True:

            self.RunFullSC_listener.run()
        elif self.RunFullSC_swc.value == False:

            self.RunFullSC_listener.stop()
        pass

    def HotKey_KillSCR(self, *e):
        """快捷键截图开关触发函数"""
        # print("DEBUG e obj > ",e)
        if self.KillSCR_swc.value == True:
            # print("DEBUG 启动了屏幕截图监听")

            self.KillSCR_listener.run()

        elif self.KillSCR_swc.value == False:
            # print("DEBUG 停止了屏幕截图监听")
            self.KillSCR_listener.stop()
        pass

    def hotkey_runwindows(self, *e):
        if self.runwindows_swc.value == True:

            self.runwindows_lis.run()

        elif self.runwindows_swc.value == False:
            self.runwindows_lis.stop()
        pass

    def selPages_Helper(self, index):
        """帮助切换页面选择器"""
        self.NowSelIndex = str(index)
        self.pickrandomyiyan()

        exc = "ToolBox.SWC_MainPages_" + str(index) + "()"
        eval(exc)

    def SWC_MainPages_0(self):
        """切换至页面0_进程管理页面"""

        self.mmpc_Stext.value = "未知 (点我更新状态)"

        if self.loaded_bg == True:
            # print("\n[DEBUG] Loaded with BG\n")
            bgb = ft.Stack(controls=[self.col_imgbg, self.funcTab_Stuff])

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=0), bgb],
                height=self.page.window_height,
                width=self.page.window_width,
            )

            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

        else:
            # print("\n[DEBUG] UnLoaded with BG\n")
            # nedadd = ft.Row([self.MyRail , ft.VerticalDivider(width=1),ft.Column([self.yiyanshowtext,self.funcTab_Stuff])],expand=True)
            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), self.funcTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
            )
            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()
        pass

    def SWC_MainPages_1(self):
        """切换至页面1_其他管理页面"""
        # print("Func Run SWC 1")

        if self.loaded_bg == True:
            # print("\n[DEBUG] Loaded with BG\n")
            bgb = ft.Stack(controls=[self.col_imgbg, self.func_SecondTab_Stuff])

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=0), bgb],
                height=self.page.window_height,
                width=self.page.window_width,
            )

            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

        else:
            # print("\n[DEBUG] UnLoaded with BG\n")
            # nedadd = ft.Row([self.MyRail , ft.VerticalDivider(width=1),ft.Column([self.yiyanshowtext,self.funcTab_Stuff])],expand=True)
            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), self.func_SecondTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
            )
            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

        pass

    def Get_yccmd_loj(self, *e):
        """获取远程控制命令的逻辑触发函数"""
        get = get_yuancheng_cmd()
        if get == None:
            self.show_snakemessage("未拦截到控制命令参数")
        else:
            bcmd = build_run_srcmd(YC_command=get)
            runcmd(bcmd)
            # fix 黑框
        pass

    def replace_SCR_loj(self, *e):
        """替换SCR程序为拦截程序的逻辑触发函数"""
        ser_status = check_MMPC_status()
        if ser_status == False:
            self.show_snakemessage("开始替换程序 请稍等...\n这大约需要6秒左右")
            status = replace_ScreenRender()
            if status == False:
                self.show_snakemessage(
                    "替换拦截程序失败 未检测到可替换程序\n请确保ScreenRender_Helper.exe\n与工具箱处在同一目录"
                )
            else:
                self.show_snakemessage("理论上已经成功替换拦截程序\n可自行检查替换结果")
        else:
            self.show_snakemessage("替换拦截程序失败\n请先手动关闭学生端根服务！")

    def restone_SCR_loj(self, *e):
        """恢复SCR程序的逻辑触发函数"""
        ser_status = check_MMPC_status()
        if ser_status == False:
            self.show_snakemessage("开始还原替换程序 请稍等...")
            status = restone_ScreenRender()
            if status == False:
                self.show_snakemessage(
                    "尝试恢复拦截程序时失败\n未检测到被重命名的ScreenRender.exe"
                )
            else:
                self.show_snakemessage("理论上已经成功恢复原有程序")
        else:
            self.show_snakemessage("还原拦截程序失败\n请先手动关闭学生端根服务！")

    def dev_read_lj_cmd_loj(self, *e):
        """读取已拦截的命令逻辑触发函数"""
        status = save_now_yccmd()
        if status == None:
            self.show_snakemessage("未拦截到控制命令参数")
        else:
            self.show_snakemessage("保存拦截命令成功")

    def update_replace_status(self, *e):
        """更新替换程序状态检查"""

        if check_tihuan_SCRY_status():
            self.show_snakemessage("检测到目录下已有ScreenRender_Y.exe")
            self.replace_status.value = "已替换"
        else:
            self.show_snakemessage(
                "未检测到ScreenRender_Y.exe\n也许未执行替换或替换过程被打断"
            )
            self.replace_status.value = "未替换"

        self.page.update()

    def SWC_MainPages_2(self):
        """切换至页面2_控屏管理界面"""

        self.replace_status = ft.TextField(
            label="替换程序状态",
            value="未知 (点我更新状态)",
            read_only=True,
            on_focus=self.update_replace_status,
            text_align=ft.TextAlign.CENTER,
        )

        self.ConlTab_Stuff = ft.Column(
            [
                self.yiyanshowtext,
                ft.Divider(height=1),
                self.col_readme_dig,
                self.replace_status,
                self.tihuan_scr,
                self.try_read_sharecmd,
                self.RunFullSC_btn,
                self.KillSCR_btn,
                self.restone_scr,
                self.runwindows_swc,
                self.KillSCR_swc,
                self.RunFullSC_swc,
            ]
        )

        if self.loaded_bg == True:

            bgb = ft.Stack(controls=[self.col_imgbg, self.ConlTab_Stuff])

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), bgb],
                height=self.page.window_height,
                width=self.page.window_width,
            )

            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

            self.added_pickdialog()

        else:

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), self.ConlTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
            )
            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

            self.added_pickdialog()
        pass

    def SWC_MainPages_3(self):
        """切换至页面3_外观调整界面"""

        if self.loaded_bg == True:

            bgb = ft.Stack(controls=[self.col_imgbg, self.waiguanTab_Stuff])

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), bgb],
                height=self.page.window_height,
                width=self.page.window_width,
            )

            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

            self.added_pickdialog()

        else:

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=1), self.waiguanTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
            )
            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

            self.added_pickdialog()

        pass

    def SWC_MainPages_4(self):
        """切换至页面4_关于界面"""

        self.AboutTab_Stuff = ft.Column(
            controls=[
                ft.Text("此工具箱在Github上发布", size=22),
                ft.Text("愿我们的电脑课都不再无聊~🥳", size=22),
                ft.ElevatedButton("点我打开工具箱Github页", on_click=opengithubres),
                ft.VerticalDivider(width=2),
                self.conl_save_ycCmd_input,
                self.conl_ycCmd_update,
                self.teachIp_input,
                self.auto_gennerate_cmd,
                self.conl_getyccmd_btn,
            ]
        )

        if self.loaded_bg == True:

            bgb = ft.Stack(controls=[self.col_imgbg, self.AboutTab_Stuff])

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=0), bgb],
                height=self.page.window_height,
                width=self.page.window_width,
            )

            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

        else:

            nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=0), self.AboutTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
            )
            self.page.clean()
            self.page.update()
            self.page.add(nedadd)
            self.page.update()

    def SWC_MainPages_5(self):
        """切换至页面5"""
        self.dllname_input = ft.TextField(label="File FullName")
        # Dll 名称 如: xxx.dll
        self.dll_func_input = ft.TextField(label="Function Name")
        # Dll 内的导出函数 如: GetUserNameA
        self.dll_return_input = ft.TextField(label="Return Type")
        # 返回值的类型 bool , int , char , long , double
        
        self.dll_confirm_btn = ft.FilledTonalButton(
            text="Confirm",
            on_click=lambda _: dev_test_use_dll(
                self.dllname_input.value,
                self.dll_func_input.value,
                self.dll_return_input.value,
                ),
            icon=ft.icons.CODE,
        )
        
        self.debugTab_Stuff = ft.Column(
            controls=[
                ft.Text("在操作前请确保你知道参数应该填什么",size=19,color="red"),
                self.dllname_input,
                self.dll_func_input,
                self.dll_return_input,
                self.dll_confirm_btn,
            ]
        )
        
        nedadd = ft.Row(
                [self.MyRail, ft.VerticalDivider(width=0), self.debugTab_Stuff],
                height=self.page.window_height,
                width=self.page.window_width,
        )

        self.page.clean()
        self.page.update()
        self.page.add(nedadd)
        self.page.update()

    def added_pickdialog(self):
        """添加文件选择对话框"""
        for idlg in self.list_all_pickdialog:
            self.page.add(idlg)
            self.page.update()

    def reflashbg(self):
        """刷新背景"""

        ToolBoxCfg.set_style_path("bgPath", self.bgpath)

        self.loaded_bg = True
        self.col_imgbg = ft.Image(
            src=f"{self.bgpath}",
            height=self.page.window_height,
            width=self.page.window_width - 100,
            opacity=self.bgtmd,
            fit=ft.ImageFit.SCALE_DOWN,
        )

        exc = "ToolBox.SWC_MainPages_" + self.NowSelIndex + "()"

        eval(exc)

    def guaqi_chufa(self, *e):
        """用于挂起进程开关的触发函数"""
        if self.guaqi_runstatus == False:
            self.page.window_visible = False
            self.page.update()
            status = guaqi_process(ToolBoxCfg.studentExeName)

            status_ = guaqi_process("MultiClient.exe")

            if status == True:
                self.guaqi_runstatus = True
                time.sleep(0.8)
                self.page.window_visible = True
                self.page.update()
            else:
                self.page.window_visible = True
                self.guaqi_sw.value = False
                self.page.update()
                self.show_snakemessage(status)
        else:
            status = huifu_process(ToolBoxCfg.studentExeName)
            status_ = huifu_process("MultiClient.exe")
            if status == True:
                self.guaqi_runstatus = False
            else:
                self.guaqi_sw.value = False
                self.page.update()
                self.show_snakemessage(status)

    def forunlocknettips(self, *e):
        self.show_snakemessage("解锁网络锁定中 请稍等")
        unlockedNet()
        self.show_snakemessage("执行完成 理论上网络已解锁")

    def usb_unlock_tips(self, *e):

        if not check_MMPC_status():
            self.show_snakemessage(
                "尝试解锁USB... 请稍等 \n实验性功能 未进行实机测试 可能无效"
            )

            usb_unlock()
        else:
            self.show_snakemessage("请先关闭学生端根服务")

    def pickrandomyiyan(self, *e):
        """挑选一个随机一言"""

        if self.defult_yy == False:
            # 如果已经加载了外部一言
            pickindex = random.randint(0, self.ex_fullindex - 1)
            self.yiyanshowtext.value = self.yiyanlist[pickindex]
            self.yiyanshowtext2.value = self.yiyanlist[pickindex]

            self.page.update()
        elif self.defult_yy == True:
            deft_yiyanlist = [
                "人生苦短,我用Python",
                "亻尔 女子",
                "《机房课时间管理》",
                "就让你看看...这葫芦里卖的什么药！",
                "让我来摸个鱼吧~",
            ]
            deft_pickindex = random.randint(0, 4)
            self.yiyanshowtext.value = deft_yiyanlist[deft_pickindex]
            self.yiyanshowtext2.value = deft_yiyanlist[deft_pickindex]

            self.page.update()

        pass

    def show_snakemessage(self, showtext: str):
        """展示一条底部消息"""

        self.page.snack_bar = ft.SnackBar(ft.Text(showtext))
        self.page.snack_bar.open = True

        self.page.update()

    def loadyiyan(self):
        """从外部加载一言库"""
        ToolBoxCfg.set_style_path("yiyanPath", self.yiyanfpath)

        try:
            fm = open(self.yiyanfpath, "r", encoding="utf-8")
            get = fm.read()
            fm.close()

            list_get = get.split("^")

            self.ex_fullindex = len(list_get)

            self.yiyanlist = list_get

            self.defult_yy = False  # 关闭默认一言库

            self.show_snakemessage("成功加载外部一言库")

        except Exception as e:
            self.show_snakemessage(f"加载外部一言时出现{e}异常")
        pass

    def change_bg_btmd(self, e):
        """改变背景图片不透明度的信号触发函数"""
        self.bgtmd = e.control.value
        self.reflashbg()

    def yiyan_pick_files_result(self, e: ft.FilePickerResultEvent):

        try:
            _yiyanfpath = e.files[0]
            self.yiyanfpath = os.path.join(_yiyanfpath.path)
            self.loadyiyan()

        except TypeError:
            self.show_snakemessage("未选择一言文件")
        pass

    def setup_zidingyi_font(self):
        """设置自定义字体"""

        ToolBoxCfg.set_style_path("fontPath", self.zdy_fontpath)

        self.font_loadtime += 1
        print("[DEBUG] font_loadtime var = ", self.font_loadtime)
        # 就是不知道为什么这里就直接是2了
        if 10 >= self.font_loadtime > 2:  # 删除旧的历史字体路径缓存
            # 似乎无解了 尽力了 二次修改字体就会无效
            # 牛逼 牛逼 整好了 以一种很抽象的方式解决了
            # 不知道为什么覆盖掉的值不能用就很离谱
            # print("Try DEL Old")
            self.old_zidyingy_time = self.font_loadtime - 1

            del self.page.fonts[f"zidingyi{self.old_zidyingy_time}"]
            # SyntaxError: cannot delete function call
        elif self.font_loadtime > 10:
            self.old_zidyingy_time = self.font_loadtime - 1
            del self.page.fonts[f"zidingyi{self.old_zidyingy_time}"]
            self.font_loadtime = 3
        self.page.fonts.update({f"zidingyi{self.font_loadtime}": self.zdy_fontpath})
        self.page.theme = ft.Theme(font_family=f"zidingyi{self.font_loadtime}")
        self.page.update()

        # sb了 不是普通括号
        if self.loaded_bg == True:  # 防止在新加载字体时把背景冲掉

            self.reflashbg()

    def font_pick_files_result(self, e: ft.FilePickerResultEvent):
        try:
            _fontfpath = e.files[0]
            self.zdy_fontpath = os.path.join(_fontfpath.path)
            self.setup_zidingyi_font()

        except TypeError:
            self.show_snakemessage("未选择字体文件")
        pass

    def pick_files_result(self, e: ft.FilePickerResultEvent):
        try:
            _bgpath = e.files[0]
            self.bgpath = os.path.join(_bgpath.path)
            self.bgtmdb.disabled = False
            self.reflashbg()
        except TypeError:
            self.show_snakemessage("未选择背景图片")
            pass

    def only_update_MMPC_status(self, *e):
        """仅更新MMPC根服务状态"""
        st = check_MMPC_status()
        if st == True:
            self.mmpc_Stext.value = "正在运行"
            self.page.update()
        elif st == False:
            self.mmpc_Stext.value = "未运行"
            self.page.update()

    def MMPC_shutdown_start_chufa(self, *e):
        """关闭/开启MMPC根服务的触发函数"""
        st = check_MMPC_status()
        if st == True:

            runcmd("sc stop MMPC")
        elif st == False:

            runcmd("sc start MMPC")


ToolBox = Ui()


ft.app(target=ToolBox.main)
