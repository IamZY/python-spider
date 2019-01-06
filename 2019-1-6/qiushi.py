# -*-coding:utf-8 -*-

import urllib2
from lxml import etree
import json

url = "https://www.qiushibaike.com/text/page/1/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    }

request = urllib2.Request(url,headers=headers)

html = urllib2.urlopen(request).read()

text = etree.HTML(html)

# //div[contains(@id,"qiushi_")]/div/a/h2/text()
# 模糊查询方法
node_list = text.xpath('//div[contains(@id,"qiushi_")]')

# print node_list

item = {}

for node in node_list:
    username = node.xpath('./div/a/h2/text()')

    content = node.xpath('.//div[@class="content"]/span/text()')

    item = {
        "username":username,
        "content":content
    }

    with open("duanzi.json","a") as f:
        f.write(json.dumps(item,ensure_ascii=False).encode("utf-8"))




