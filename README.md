
![ToolBox_logo](https://github.com/user-attachments/assets/98db71e1-14e3-420c-9617-896179bed8d7)

---

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ZiHaoSaMa66/OsEasy-ToolBox?label=%E6%9C%80%E6%96%B0%E7%89%88&style=for-the-badge&include_prereleases&color=pink)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/releases)
[![GitHub release](https://img.shields.io/github/release/ZiHaoSaMa66/OsEasy-ToolBox.svg?color=green&style=for-the-badge&label=%E7%A8%B3%E5%AE%9A%E7%89%88)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/releases/latest)
![GitHub all releases download](https://img.shields.io/github/downloads/ZiHaoSaMa66/OsEasy-ToolBox/total?style=for-the-badge&label=%E6%80%BB%E4%B8%8B%E8%BD%BD%E9%87%8F&color=orange)
![GitHub Repo stars](https://img.shields.io/github/stars/ZiHaoSaMa66/OsEasy-ToolBox?style=for-the-badge&color=yellow)

> [!IMPORTANT]
> **工具箱需要以管理员权限运行!**   
> 适用于``V10.8.2.4411``桌面云环境的噢易学生端      
> 如果系统为 **windows 7** 请使用[轻量版工具箱! (已暂时摆烂停更)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox-Lite)     


## 免责声明

本项目仅供**教育研究**和**技术学习**目的，旨在学习研究软件运行机制和原理而生，禁止用于任何非法用途。   
本软件包含可能影响系统稳定的实验性代码，操作不当可能导致：    
系统数据丢失或损坏、应用程序异常崩溃等，使用者需自行承担所有操作风险，使用前应做好完整系统备份。
 
开发者/贡献者不对以下情况负责：
- 因使用本项目造成的直接/间接损失
- 违反用户所在机构相关规定导致的后果
- 因软件使用导致的任何法律纠纷

**继续使用即表示您已充分阅读、理解并同意承担所有相关风险及法律责任**

## 🚀 快速开始

> [!IMPORTANT]    
> 在`V10.9.0.4881`的学生端使用时     
> 遇到脚本提示拒绝访问则需要**停止学生端根服务**     
> 如果你发现学生端没有自动重启可以手动重启服务     
> ***不保证功能在其他版本的噢易学生端中均可用***    

### **[点我看工具箱功能演示视频! (BiliBili)](https://www.bilibili.com/video/BV12ZgeetEWr)**

> 简单说下我的使用过程     
> 具体如何使用看实际情况 仅供参考    


1. **解除学生端自带的键鼠锁定 断网锁定 远程控制**

   `其他管理 -> 删除键盘锁驱动&控屏锁定程序&黑屏安静 -> 三者一起删除`      
   等待删除完毕后 可以按任意按键跳过注销脚本的等待    
   待注销完毕后回到登录回来继续步骤
   * 有人说学生端不再会自启动 如果要恢复学生端    
   长按 `进程管理 -> 开关学生端根服务`    
   如果机器太卡可自己开 cmd 运行 `sc start mmpc`    
     

2. **解锁网络限制**    

   `其他管理 -> 解除网络限制锁`     
   或者 `DLL工具 -> 执行:关闭网络管控`
   如果老师平时不锁网络可以跳过这一步     
   如果不需要广播管理等功能可以直接跳过下面的步骤     
   直接 `进程管理 -> 挂起学生端主进程` 挂起进程后直接开玩 (
      

3. **配置外置屏幕广播**
   
   点击任务栏处的学生端 在弹出的菜单中点击设置 查看其教师机IP地址    
   `广播命令 -> 输入教师机IP` 把看到的IP抄进去     
   随后按 `由教师机IP生成广播命令`     
   接着打开`广播管理`的快捷键相关选项

   **可能会出现的问题**    
   工具箱获取到的本机IP地址不正确    
   你需要使用`读取已拦截的广播命令`自行修改其`#local#`的值为本机IP    
   接着粘贴到上一个输入框中 随后 `手动更新广播命令`


4. **最后**   

   `进程管理 -> 挂起学生端主进程`    
   至此完成全部功能的配置
   


> 可能某些功能上手用的时候会有点抽象     
> (理解理解.jpg)   

想要定制自己的的一言?   

[点我查看外部一言格式说明!](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/blob/main/外部一言格式说明.md)

----

### ✨ 上机实战效果截图

**效果图中老师均使用了全屏广播**    
通过工具箱的拦截广播命令实现的     
**无视全屏广播**手动打开窗口广播     

<details>
<summary>点击展开查看截图</summary>

![批注 2024-05-30 172101](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/bd62df84-db76-4c0e-a591-c24ea8fdbab2)

![批注 2024-06-13 171855](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/7845f270-824f-4399-92f9-2ff6b7e2f3d6)

> 很早就想截了 但是一拖再拖(     

</details>

----

### 👀 工具箱界面截图   
<details>
<summary>点击展开查看截图</summary>
  
![1](https://github.com/user-attachments/assets/d9b8b8bf-9a82-4ca7-b0a7-822d230b4910)

![2](https://github.com/user-attachments/assets/9b55ea88-4752-4e13-8be2-3ee4698dbcd0)

![3](https://github.com/user-attachments/assets/0c5d8c07-8538-45ee-8d84-c302ce4e8634)

![4](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/3b011ff9-1808-4a26-81e2-89d72bccf383)

![5](https://github.com/user-attachments/assets/3aa601da-56d1-4a5f-9a63-642722c1cb7f)


</details>

----

### 🌈 最后的最后..
如果你喜欢我的破工具箱可以点个⭐Star⭐   
感谢有你们的Star鼓励和支持💖     

有问题&发现Bug&提供建议可以提提issue     
同时如果你有兴趣也可以开开PR    
愿我们的电脑课都不再无聊~🥳   
