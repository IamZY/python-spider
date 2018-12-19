# -*- coding:utf-8 -*-

import urllib
import urllib2

# http://tieba.baidu.com/f?kw=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2&ie=utf-8&pn=100

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
    }


def loadPage(url,filename):
    '''
    跟怒url 发送数据请求 获取服务器响应文件
    url 爬取网站
    filename 处理的文件名
    :return:
    '''
    print "正在下载" + filename
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    return response.read()


def writePage(html,filename):
    '''
    将html写入本地
    :return:
    '''
    print "正在保存..." + filename

    with open(filename.decode("utf-8"), "w") as f:
        f.write(html)
    print "-" * 30

def tiebaSpider(url, beginPage, endPage):
    '''
    贴吧爬虫调度器
    :return:
    '''
    for page in range(beginPage,endPage + 1):
        pn = (page - 1)*50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        html = loadPage(fullurl,filename)
        writePage(html,filename)
        print "谢谢使用..."


if __name__ == "__main__":
    kw = raw_input("请输入需要爬去的贴吧名")
    beginPage = raw_input("请输入起始页")
    endPage = raw_input("请输入结束页")
    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw":kw})

    fullurl = url + key

    tiebaSpider(fullurl,int(beginPage),int(endPage))


