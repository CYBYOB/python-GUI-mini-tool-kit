# coding: utf-8

# 爬虫所需的类、方法属性等

import re
import requests
from selenium import webdriver

class Crwaler():

    def __init__(self, url):
        # url = 'https://wenku.baidu.com/view/d7de31cf763231126edb11d2.html'
        self.url = url
        self.response = ''
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', chrome_options=chrome_options)
        self.driver.implicitly_wait(30)

    # 通过 selenium 库获取 网页源码
    def getHtmlBySelenium(self):
        self.driver.get(self.url)
        self.response = self.driver.page_source

    # 删除网页中多余的 HTML 标签
    def deleteHtmlTag(self):
        pattern = re.compile(r'<[^>]*>', re.S)
        newResponse = pattern.sub(' ', self.response)
        return newResponse


