# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

# 通过CookieJar() 构建对象 用来保存Cookie的值
cookie = cookielib.CookieJar()

# 通过Http处理Cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)

# 元组
opener.addheaders = [
    ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0")
]

# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
# }

data = {
    "email":"********",
    "password":"********"
}

# 通过urlencode转码
data = urllib.urlencode(data)

# 人人网的登录接口
url = "http://www.renren.com/PLogin.do"

# response = urllib2.Request(url,data=data,headers=header)
# 第一次是post请求 发送登录需要的额参数 获取Cookie
request = urllib2.Request(url,data=data)

response = opener.open(request)
# 获取登录的页面信息
print response.read()

