# -*- coding:utf-8 -*-

import urllib2


# 向指定的url地址发动请求
response = urllib2.urlopen("http://www.baidu.com/")

# 服务器返回的类文件对象支持Python文件对象的操作方法
# 读取文件中的内容 返回字符串
html = response.read()

# 打印响应内
'''
默认User-Agent:Python-urllib
'''
print html