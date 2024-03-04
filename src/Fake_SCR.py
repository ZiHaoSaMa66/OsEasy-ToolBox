import sys
# 假ScreenRender.exe

MLsavepath = "C:\\Users\\Administrator\\prod\\SCCMD.txt"

# if len(sys.argv) >=4:
#     print("? ERR > len(sys.argv) >=4:")
#     sys.exit(1)

# get = sys.argv[1]
emp = []
for i in sys.argv:
    # print("debug > ",i)
    emp.append(i)

# print("emp > ",emp)
# "C:\Program Files (x86)\Os-Easy\os-easy multicast teaching system\ScreenRender.exe" {#decoderName#:#h264#,#fullscreen#:0,#local#:#172.18.36.132#,#port#:7778,#remote#:#229.1.36.200#,#teacher_ip#:0,#verityPort#:7788}
# get = str(get)


for data_ in emp:
    data = str(data_)
    repcmd = data.replace("#fullscreen#:1","#fullscreen#:0").replace(" ","")


fm = open(MLsavepath,"w")
fm.write(str(repcmd))
fm.close()
# print(f"\n\nGET_CMD >>>{repcmd}\n\n")
print("拦截命令成功 你可以暴力脱离控制")
print("并使用广播管理页的功能了")
