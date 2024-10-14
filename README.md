![OsEasy-ToolBox](https://socialify.git.ci/ZiHaoSaMa66/OsEasy-ToolBox/image?description=1&descriptionEditable=A%20Simple%20Python%20ToolBox%20for%20OsEasyTeachingSystem&font=Source%20Code%20Pro&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F134737096&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark)

---

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ZiHaoSaMa66/OsEasy-ToolBox?label=%E6%9C%80%E6%96%B0%E7%89%88&style=for-the-badge&include_prereleases&color=pink)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/releases)
[![GitHub release](https://img.shields.io/github/release/ZiHaoSaMa66/OsEasy-ToolBox.svg?color=green&style=for-the-badge&label=%E7%A8%B3%E5%AE%9A%E7%89%88)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/releases/latest)
![GitHub all releases download](https://img.shields.io/github/downloads/ZiHaoSaMa66/OsEasy-ToolBox/total?style=for-the-badge&label=%E6%80%BB%E4%B8%8B%E8%BD%BD%E9%87%8F&color=orange)
![GitHub Repo stars](https://img.shields.io/github/stars/ZiHaoSaMa66/OsEasy-ToolBox?style=for-the-badge&color=yellow)

> [!TIP]  
> 推荐优先使用稳定版    
> 最新版拥有新特性    
> 但是可能存在潜在未发现的Bug     
> ~~稳定版也保不准没有bug（）~~          

> [!IMPORTANT]
> **工具箱需要以管理员权限运行!**   
> 适用于``V10.8.2.4411``桌面云环境的噢易学生端      
> 如果你学校的电脑是**win7系统**的请使用[轻量版工具箱! (已暂时摆烂停更)](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox-Lite)     
>        

> 这是一些~~废话~~(     
> 网上几乎搜不到针对噢易的有效制裁工具     
> (至少在我着手开发的时候是没找到一点..)     
> (搜到的都是什么~~人机~~噢易的官网)    
> 搜来搜去实在找不到只能自己动手丰衣足食了   
> 但是只能说勉强能用 哥们编程也就那样了💦💦    
> 至少我自己的电脑课上是能用的😎       
 
### **[点我看工具箱功能演示视频! (BiliBili)](https://www.bilibili.com/video/BV12ZgeetEWr)**


## 🚀 快速开始 脱控摸鱼!

> [!IMPORTANT]    
> 在`V10.9.0.4881`的学生端使用时     
> 遇到脚本提示拒绝访问则需要**停止学生端根服务**     
> 如果你发现学生端没有自动重启可以手动重启服务     
> ***不保证功能在其他版本的噢易学生端中均可用***     

> 简单说下我的使用过程     


1. `其他管理 -> 删除键盘锁驱动&控屏锁定程序&黑屏安静 -> 三者一起删除`      
   等待删除完毕后 可以按任意按键跳过注销脚本的等待    
   待注销完毕后回到登录回来继续步骤    
     

2. `其他管理 -> 解除网络限制锁`    
   如果老师平时不锁网络可以跳过这一步     
   如果不需要广播管理等功能可以直接跳过下面的步骤     
   直接 `进程管理 -> 挂起学生端主进程` 挂起进程后直接开玩 (
      

3. `屏幕广播管理 -> 替换拦截广播命令程序`    
   此时只需要等待老师广播一次就可以拦截到广播命令了     
   如果**有需要**可以提前 使用 `进程管理 -> 替换粘滞键为cmd脚本`    
   来快捷强制关闭学生端     
   **如果你在上一次已经完成了第4步可以直接跳过这一步**     


4. `关于 -> 长按打开工具箱Github页面 -> 读取已拦截的广播命令`     
    工具箱所在目录下会生成一个command.txt文件     
    下次上机时你可以直接将command.txt文件内容复制到`输入广播命令`输入框中     
    最后 `关于 -> 长按打开工具箱Github页面 -> 手动更新广播命令`     

    在`v1.7 RC`后续的版本将不需要 `长按打开工具箱Github页面`     
    直接在 `关于` 页中点击对应功能即可

    确保已经有 **正确** 的命令填入输入框     
    请不要让输入框为空时 点击 `手动更新广播命令`

    你得到的广播命令的格式 应该是这样的格式
`
{#decoderName#:#h264#,#fullscreen#:0,#local#:#172.18.17.152#,#port#:7778,#remote#:#229.1.17.200#,#teacher_ip#:0,#verityPort#:7788}`

    请确保你的命令中的 `#local#` IP地址值 和 你的机器IP地址 **一致**

5. 最后打开`广播管理`的快捷键相关选项 和 `进程管理 -> 挂起学生端主进程`     
   就可以开玩了(

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
  
![屏幕截图 2023-12-22 222946](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/59f30333-b361-4b93-b6e8-37c65df228b2)

![屏幕截图 2023-12-22 223003](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/0168a6fb-16aa-428b-bf9b-6063d1623db3)

![sc5](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/3b011ff9-1808-4a26-81e2-89d72bccf383)

![屏幕截图 2023-12-22 223021](https://github.com/ZiHaoSaMa66/OsEasy-ToolBox/assets/134737096/660f4f86-b8a4-4173-87e6-9fcf5cedd052)


</details>

----

### 🌈 最后的最后..
如果你喜欢我的破工具箱可以点个⭐Star⭐   
感谢有你们的Star鼓励💖     

有问题&发现Bug&提供建议可以提提issue     
同时如果你有兴趣也可以开开PR    
愿我们的电脑课都不再无聊~🥳   
