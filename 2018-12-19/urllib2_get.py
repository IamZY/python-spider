# -*- coding:utf-8 -*-

import urllib
import urllib2


url = "http://www.baidu.com/s"

keyword = raw_input("输入关键字")

wd = {"wd": keyword}

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/64.0"}

wd = urllib.urlencode(wd)

fullurl = url + "?" + wd

request = urllib2.Request(fullurl,headers = headers)

response = urllib2.urlopen(request)

print response.read()