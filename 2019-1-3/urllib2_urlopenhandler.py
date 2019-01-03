# -*- coding:utf-8 -*-

import urllib2

# 构建处理器对象 处理请求
http_handler = urllib2.HTTPHandler()

# 会自动打开debug log 模式 程序执行的时候会打印收发包的信息
# http_handler = urllib2.HTTPHandler(debuglevel=1)

# 构建自定义opener
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)

print response.read()