#-*- coding=utf-8 -*-

import urllib2
import re

class Spider:
    def __init__(self):
        # 初始化页面位置
        self.page = 2
        # 爬取开关 true 继续爬取
        self.switch = True

    def loadPage(self):
        """
        下载页面
        :return:
        """
        url = "https://www.neihan8.com/article/index_"+ str(self.page) +".html"
        # url = "https://www.neihan8.com/article/index_2.html"

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
        }
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        # print html
        # '<div>\sclass="desc">(.*?)</div>'
        # 全文匹配
        pattern = re.compile('<div\sclass="desc">(.*?)</div>',re.S)
        # 将正则怕匹配对象返回所有段子的集合
        content = pattern.findall(html)
        # print content
        # for c in content:
            # print c.decode("utf-8")
            # print c
        self.dealPage(content)

    def dealPage(self,content):
        """
        处理每页的段子
        :return:
        """
        for item in content:
            self.writePage(item)


    def writePage(self,item):
        """
        把每条段子逐个写入文件
        :return:
        """
        with open("duanzi.txt","a") as file:
            file.write(item+"\n")


    def startWork(self):
        """
        控制爬虫的运行
        :return:
        """
        while self.switch:
            command = raw_input("如果继续爬取，请按回车，退出输入quit")
            if command == "quit":
                self.switch = False
            self.loadPage()
            self.page += 1



if __name__ == "__main__":
    duanziSpider = Spider()
    # duanziSpider.logePage()
    duanziSpider.startWork()