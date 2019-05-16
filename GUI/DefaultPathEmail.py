# coding: utf-8

import tkinter as tk
import tkinter.messagebox
from tkinter.filedialog import askdirectory

import sys
sys.path.append('../')
import Global


# 设置默认 路径 和  收件箱 很相似，抽象出一个基类

class PathEmail(tk.Tk):
    def __init__(self, title, textLabel, textEntry, textBtn):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title(title)

        tk.Label(self, text=textLabel).pack()
        # 之前传过来的窗口
        # self.preWindow = preWindow
        # self.preWindow.withdraw()

        self.default = tk.StringVar()
        self.defaultEntry = tk.Entry(self, textvariable = self.default, width=300)
        self.defaultEntry.pack()
        print(textEntry)
        self.default.set(textEntry)

        tk.Button(self, text=textBtn, command=lambda: self.setDefault()).pack()

        # 当前窗口点了 X 之后
        # self.protocol('WM_DELETE_WINDOW', self.closeWindow)

    # 当前窗口点了 X 之后
    # def  closeWindow(self):
    #     self.destroy()
    #     self.preWindow.deiconify()

    # 该函数需要重载
    def setDefault(self):
        pass

class Path(PathEmail):
    # def __init__(self, title, textLabel, textEntry, textBtn):
    #     PathEmail.__init__(self, title, textLabel, textEntry, textBtn)

    def setDefault(self):
        print(self.defaultEntry.get())
        path = askdirectory()
        print(type(path))
        # 只有 文件路径长度不为 0 ，说明没有点击取消，同时更新 路径框的值和 全局的 defaultPath
        if (len(path) > 0):
            Global.defaultPath = path
            self.default.set(path)
            print(self.default.get())
            # 弹出提示框，更改成功
            tk.messagebox.showinfo(message='更改默认路径成功！当前路径：'+self.default.get())
            print(self.defaultEntry.get())
            print('Global:', Global.defaultPath)
            self.withdraw()



class Email(PathEmail):

    def setDefault(self):
        # 对进行填写的 收件箱进行合法性判断，这里应该用 正则等，但为了简单起见就不用了
        if(len(self.default.get()) == 0 ):
            tk.messagebox.showwarning('设置失败', '收件箱不能为空！')
        else:
            Global.defaultEmail = self.default.get()
            tk.messagebox.showinfo('设置成功！', '当前收件箱为'+self.default.get())
            print(Global.defaultEmail)
        # self.withdraw()


if __name__ == '__main__':
    # b = tk.Tk()
    a = Path( '默认', '默认', Global.defaultPath, '默认')


    a.mainloop()