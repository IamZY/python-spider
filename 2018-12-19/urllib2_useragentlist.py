# -*- coding:utf-8 -*-

import urllib2
import random
import urllib

url = "http://www.baidu.com/"

# 可以是user-agent列表 或者是代理列表
ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
]

user_agent = random.choice(ua_list)

request = urllib2.Request(user_agent)

request.add_header("User-Agent",user_agent)

# 只有第一个字母是大写 其他的都是小写
print request.get_header("User-agent")

wd = {"wd":"传智播客"}

urllib.urlencode(wd)



# https://www.baidu.com/s?wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2