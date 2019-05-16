# coding:utf-8

# 有些问题尚未解决， py 留下了编码的眼泪！！

import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import messagebox


class Poem(tk.Tk):
    def __init__(self, preWindow):
        tk.Tk.__init__(self)
        # 隐藏之前的窗口，若当前窗口被点击了 "X" 以退出当前窗口 ==》  摧毁当前窗口，显示之前的窗口
        self.preWindow = preWindow
        self.preWindow.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.closeWindow)
        self.title('古诗生成器')
        self.geometry('500x500')

        num = [('五字', '5'), ('七字', '7')]
        self.varNum = tk.StringVar()
        tk.Label(self,text='一句诗的字数:').pack()
        for text, value in num:
            tk.Radiobutton(self, text=text, value=value, variable=self.varNum).pack()
        self.varNum.set('5')
        position = [('藏头', 'head'), ('藏尾', 'tail')]
        self.varPosition = tk.StringVar()
        self.varPosition.set('head')
        tk.Label(self, text='藏头还是藏尾:').pack()
        for text, value in position:
            tk.Radiobutton(self, text=text, value=value, variable=self.varPosition).pack()

        # 输入的诗句内容
        self.varText = tk.StringVar()
        self.poemText = tk.Entry(self, textvariable=self.varText)
        self.poemText.pack()

        # 提交按钮
        tk.Button(self, text='提交', command=lambda: self.commit()).pack()

    # 关闭当前窗口，回复之前的窗口
    def closeWindow(self):
        self.destroy()
        self.preWindow.deiconify()

    # 一句诗的字数
    def getNum(self):
        return self.varNum.get()

    # 藏头还是藏尾
    def getPosition(self):
        return self.varPosition.get()

    # 获得输入的诗句内容
    def getText(self):
        return self.poemText.get()

    # 提交按钮
    def commit(self):
        print(self.getNum())
        import requests
        import json

        # 填入的诗句内容不能为空
        if(len(self.poemText.get()) == 0):
            tk.messagebox.showwarning('提交失败', '诗句内容不能为空！')
            return
        url = 'http://www.520cyb.cn/mini/mini_tool_kit/poem/poem_create.php?text=' + self.getText() + '&num=' + self.getNum() + '&position=' + self.getPosition()
        print(url)
        response = requests.get(url=url).content
        new_response = json.loads(response, encoding='gbk')
        print(new_response)

        # 进行完整诗句的拼接
        poem = ''
        for i in range(int(self.getNum())-1):
            print(i)
            # 说明有诗句，不为空！
            if(isinstance(new_response[str(i)], list)):
                print(new_response[str(i)])
                poem += (new_response[str(i)][0]['line']+'\n')
            else:
                poem += '\n'

        print('poem:', poem)
        tk.messagebox.showinfo(message='诗句生成成功：\n' + poem)






if __name__ == '__main__':
    p = Poem()
    p.mainloop()

