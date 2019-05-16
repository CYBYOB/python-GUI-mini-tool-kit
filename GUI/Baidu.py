# coding: utf-8

import tkinter as tk
import tkinter.messagebox

# 导入自定义 py文件
import sys
sys.path.append('../')
import Crawler


#  GUI 百度文库、知网等，一般用于爬取这个网页的所有文本用的
class Baidu(tk.Tk):
    def __init__(self, preWindow):
        tk.Tk.__init__(self)
        # 隐藏之前的窗口，若当前窗口被点击了 "X" 以退出当前窗口 ==》  摧毁当前窗口，显示之前的窗口
        self.preWindow = preWindow
        self.preWindow.withdraw()
        self.protocol('WM_DELETE_WINDOW', self.closeWindow)
        self.title('百度、知网一键爬')
        self.geometry('500x500')


        # 保存的文件名设置
        self.fileNameLabel = tk.Label(self, text='保存的文件名（如 1 ,暂时只支持 txt 格式）：')
        self.filname = tk.StringVar()
        self.fileNameEntry = tk.Entry(self, textvariable=self.filname)
        # 添加 GUIBaidu 相关的组件与布局
        self.linkLabel = tk.Label(self, text='链接:')
        self.link = tkinter.StringVar()
        self.linkEntry = tk.Entry(self, textvariable=self.link)
        # 清除输入的链接和 下载的 按钮
        # 清除链接有 bug
        # self.clearLinkBtn = tk.Button(self, text='清除输入的链接', command= lambda : self.clickclearLinkBtn())
        self.downloadLinkBtn = tk.Button(self, text='下载', command= lambda : self.clickdownloadLinkBtn())



        self.fileNameLabel.place(relx=0.1, rely=0.3)
        self.fileNameEntry.place(relx=0.6, rely=0.3, relwidth=0.3)
        self.linkLabel.place(relx=0.1, rely=0.4)
        self.linkEntry.place(relx=0.2, rely=0.4, relwidth=0.7)
        # self.clearLinkBtn.place(relx=0.1, rely=0.5)
        self.downloadLinkBtn.place(relx=0.82,rely=0.5)

    # 关闭当前窗口，回复之前的窗口
    def closeWindow(self):
        self.destroy()
        self.preWindow.deiconify()

    # 点击 清除链接 的按钮,清空之前输入的链接
    # def clickclearLinkBtn(self):
    #     print('点击清空链接')
    #     print(self)
    #     self.link.set('')

    # 点击了 下载按钮
    def clickdownloadLinkBtn(self):
        if(self.isAllComplete()):
            print('正在下载。。。')
            # 使用 Crawler 实例去下载
            crawler = Crawler.Crwaler(self.linkEntry.get())
            htmlContent = crawler.getHtmlBySelenium()
            txtContent = crawler.deleteHtmlTag()
            print('处理后的内容为：', txtContent, '正在写入文件。。。')
            try:
                print('文件名为：', self.fileNameEntry.get())
                with open(self.fileNameEntry.get() + '.txt', mode='w+', encoding='utf-8') as f:
                    f.write(txtContent)
                print('写入成功！')
                tk.messagebox.showinfo('写入文件成功！')
            except Exception as e:
                print('发生了异常：', e)

    # 判断 文件名 和 下载 链接 是否已填写
    def isAllComplete(self):
        if(len(self.fileNameEntry.get()) and len(self.linkEntry.get())):
            return True
        elif(len(self.fileNameEntry.get()) == 0):
            tk.messagebox.showwarning('警告', '文件名不能为空！')
        else:
            tk.messagebox.showwarning('警告', '链接不能为空！')
        return False


if __name__ == '__main__':
    b = tk.Tk()
    a = Baidu(b)
    a.mainloop()