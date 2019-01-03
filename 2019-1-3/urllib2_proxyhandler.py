# -*- coding:utf-8 -*-

import urllib2

# 代理开关 表示是否启用代理
proxyswitch = True

# 构建一个处理器对象 参数是字典类型 包括代理类型和代理服务器
httpproxy_handler = urllib2.ProxyHandler({"http":"202.204.121.126:80"})
# 构建没有代理的服务器对象
nullproxy_handler = urllib2.ProxyHandler({})

# 代理ip
# 202.204.121.126 	80

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)
# 构建了一个全局的opener 之后的所有的请求都可以用urlopen()方式去发送 也附带Handler的功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")

response = urllib2.urlopen(request)

print response.read()