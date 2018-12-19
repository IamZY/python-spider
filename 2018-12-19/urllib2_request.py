# -*- coding:utf-8 -*-

import urllib2


#
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"
}

# 通过Request构造请求对象
request = urllib2.Request("http://www.baidu.com/",headers = ua_headers)
# 向指定的url地址发动请求
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# 读取文件中的内容 返回字符串
html = response.read()

# 返回响应码
# print response.getcode()

# 返回实际数据的url 防止重定向的问题
# print response.geturl()

# 返回服务器响应的http报头
# print response.info()

# 打印响应内
'''
默认User-Agent:Python-urllib
'''
print html