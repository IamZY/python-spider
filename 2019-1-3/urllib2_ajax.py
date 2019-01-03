# -*- coding:utf-8 -*-

import urllib
import urllib2

# url = "https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0"
# url = "https://movie.douban.com/explore#!"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

# formdata = {
#     "type":"movie",
#     "tag":"热门",
#     "sort":"recommend",
#     "page_limit":"20",
#     "page_start":"40"
# }

# data = urllib.urlencode(formdata)

request = urllib2.Request(url,headers=header)

print urllib2.urlopen(request).read()

