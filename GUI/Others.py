# coding:utf-8

import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox

import sys
sys.path.append('../')
import Global



# 帮助相关的 GUI (使用教程 和 关于均可用）
class Help(tk.Tk):
    def __init__(self,preWindow, title, text):
        tk.Tk.__init__(self)
        self.title(title)
        self.geometry('500x500')
        # 隐藏之前的窗口
        self.preWindow = preWindow
        preWindow.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.closeWindow)

        # 相关的一堆文字
        tk.Label(self, text=text).pack()

    def  closeWindow(self):
        self.destroy()
        self.preWindow.deiconify()


if __name__ == '__main__':
    h = SetDefaultPath()
    h.mainloop()