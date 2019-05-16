# coding: utf-8

import tkinter as tk

# 设置路径，方便引入 相关的 py文件
import sys
sys.path.append('../')
import Global

# 导入自定义的 py文件
import Baidu
import Poem
import WIFICracker
import Others
import DefaultPathEmail

# GUI 首页index
class Index(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('小小工具箱')
        self.geometry('500x500')

        # 顶层菜单栏的设置
        menubar = tk.Menu(self)
        setting = tk.Menu(menubar, tearoff=0)
        setting.add_command(label='默认路径', command=self.setDeafaultPath)
        # 这个有问题，暂时不添加
        setting.add_command(label='默认收件邮箱', command=self.setDefaultEmail)
        help = tk.Menu(menubar, tearoff=0)
        help.add_command(label='使用教程', command=self.getGuide)
        help.add_command(label='关于', command=self.getAbout)

        menubar.add_cascade(label='设置', menu=setting)
        menubar.add_cascade(label='帮助', menu=help)
        self.config(menu=menubar)

        # 百度文库、知网
        self.buttonBaidu = tk.Button(self, text='百度文库、知网', command=lambda : self.clickBaidu())
        # 古诗生成器
        self.buttonPoem = tk.Button(self, text='古诗生成器', command=lambda : self.clickPoem())
        # wifi破解器
        self.buttonWIFICracker = tk.Button(self, text='wifi破解器', command=lambda: self.clickWIFICracker())
        # 通用爬虫,暂时不加
        # self.buttonCommon = tk.Button(self, text='通用爬虫', command=lambda: self.clickCommon())
        # 图片爬虫
        # self.

        # 开始布局
        self.buttonBaidu.place(relx=0.1, rely=0.1, relwidth=0.8)
        self.buttonPoem.place(relx=0.1, rely=0.2, relwidth=0.8)
        self.buttonWIFICracker.place(relx=0.1, rely=0.3 ,relwidth=0.8)
        # self.buttonCommon.place(relx=0.1, rely=0.2, relwidth=0.8)

    def setDeafaultPath(self):
        print('点击默认路径')
        pathGUI = DefaultPathEmail.Path( '设置默认路径', '当前路径', Global.defaultPath, '选择')

    def setDefaultEmail(self):
        print('点击默认收件邮箱')
        emailGUI = DefaultPathEmail.Email( '设置收件箱地址', '当前收件箱地址', Global.defaultEmail, '确定')

    def getGuide(self):
        print('点击使用教程')
        helpManual = Others.Help(self, '使用教程', '使用教程！！')

    def getAbout(self):
        print('点击关于')
        helpManual = Others.Help(self, '关于', '关于！！')

    def clickBaidu(self):
        print('点击百度、知网等')
        # 打开相应的 GUI，并将自己隐藏（要将self传过去）
        self.withdraw()

        guiBaidu = Baidu.Baidu(preWindow=self)
        guiBaidu.mainloop()

    def clickPoem(self):
        self.withdraw()

        guiPoem = Poem.Poem(preWindow=self)
        guiPoem.mainloop()

    def clickWIFICracker(self):
        self.withdraw()

        wifiCracker = WIFICracker.WIFICracker(preWindow=self)
        wifiCracker.mainloop()

    def clickCommon(self):
        print('点击通用爬虫')


if __name__ == '__main__':
    # a = Baidu.Baidu(tk.Tk())
    a = Index()

    a.mainloop()

