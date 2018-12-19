# -*- coding:utf-8 -*-

import urllib
import urllib2

# i=Python
# from=AUTO
# to=AUTO
# smartresult=dict
# client=fanyideskweb
# salt=15452219167649
# sign=2c6b1f0e1cac570b42a59902ffd12c53
# ts=1545221916764
# bv=e2a78ed30c66e16a857c5b6486a1d326
# doctype=json
# version=2.1
# keyfrom=fanyi.web
# action=FY_BY_CLICKBUTTION
# typoResult=false

'''
POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host: fanyi.youdao.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://fanyi.youdao.com/
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 260
Connection: keep-alive
Cookie: YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=-1640124854@10.168.8.63; OUTFOX_SEARCH_USER_ID_NCOO=1507747431.8738608; _ga=GA1.2.1463677230.1540867410; _ntes_nnid=dc0f43a651065305d005895aa9982658,1544236223393; JSESSIONID=aaaARhC-6C0EQaxJIygFw; ___rl__test__cookies=1545221916762

'''



headers = {
        "Host": "fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Referer": "http://fanyi.youdao.com/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        # "Content-Length": "260",
        # "Connection": "keep-alive"
}

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

data = raw_input("请输入需要翻译的文字")

formdata = {
    "i":data,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15452219167649",
    "sign":"2c6b1f0e1cac570b42a59902ffd12c53",
    "ts":"1545221916764",
    "bv":"e2a78ed30c66e16a857c5b6486a1d326",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",                                                                                     "action":"FY_BY_CLICKBUTTION",
    "typoResult":"false"
}

new_data = urllib.urlencode(formdata)

request = urllib2.Request(url,data = new_data,headers = headers)

response = urllib2.urlopen(request)

print response.read()
