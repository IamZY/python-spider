# -*- coding:utf-8 -*-

import urllib2

test = "test"

password = "123456"

webserver="120.77.182.74"

passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# 第一个realm如果没有就写None
passwordMgr.add_password(None,webserver,test,password)

handler = urllib2.HTTPBasicAuthHandler(passwordMgr)

opener = urllib2.build_opener(handler)

request = urllib2.Request("http://"+webserver)

response = opener.open(request)

print response.read()