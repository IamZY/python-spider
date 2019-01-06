# -*- coding:utf-8 -*-

import urllib2
import json
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

request = urllib2.Request(url,headers=headers)

response = urllib2.urlopen(request)

# 取出json文件的内容
html = response.read()
# 把字符串内容 格式是字符串python格式 unicode字符串
unicodestr = json.loads(html)

city_list = jsonpath.jsonpath(unicodestr,"$..name")

# print city_list
for item in city_list:
    print item

# Python形式的列表 返回是unicode字符串
# 默认转换中文为ascii格式
# ensure_ascii=False 禁用ascii码
array = json.dumps(city_list,ensure_ascii=False)

# array = json.dumps(city_list)

with open("lagou.json","w") as f:
    f.write(array.encode("utf-8"))