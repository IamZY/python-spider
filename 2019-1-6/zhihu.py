# -*-coding:utf-8 -*-

import urllib2
import urllib
from lxml import etree


def loadPage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }

    # print url

    request = urllib2.Request(url, headers=headers)
    # request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    # print html
    # with open("zhihu.html","w") as f:
    #     f.write(html)

    # 解析html dom模型为xml文档
    content = etree.HTML(html)

    # 返回所有匹配列表的集合
    link_list = content.xpath('//div[@class="List-item"]/div/div/div/span/figure/img/@src')
    for link in link_list:
        # fulllink = "https://tieba.baidu.com"+link
        # print fulllink
        print link
        # loadImage(fulllink)


def loadImage(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }
    request = urllib2.Request(link, headers=headers)
    # request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)
    # print content
    # 返回帖子中所有图片的列表集合
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # print link_list
    for link in link_list:
        # print link
        writeImage(link)


def writeImage(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }
    # 接受每个图片连接
    request = urllib2.Request(link, headers=headers)
    response = urllib2.urlopen(request)
    image = response.read()

    filename = link[-10:]

    with open("./pic/" + filename, "wb") as file:
        print "正在下载" + filename
        file.write(image)


def tiebaSpider(url):
    loadPage(url)

    print "谢谢"
    # for page in range(beginPage,endPage+1):
    #     pn = (page-1)*50
    #
    #     fullurl = url + "&pn=" + str(pn)
    #
    #     print "正在下载第"+ str(page) +"页"


if __name__ == "__main__":
    # https: // tieba.baidu.com / f?kw = lol & ie = utf - 8 & pn = 0
    # https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=50
    # tiebaName = raw_input("请输入贴吧名")
    # beginPage = int(raw_input("请输入起始页"))
    # endPage = int(raw_input("请输入末尾页"))

    url = "https://www.zhihu.com/question/56378769/answer/541201767"
    # key = urllib.urlencode({"kw": tiebaName})
    # fullurl = url + key
    tiebaSpider(url)
