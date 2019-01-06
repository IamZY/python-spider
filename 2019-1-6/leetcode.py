# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

def leetcodeLogin():
    sess = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

    # 首先获取登录页面找到 需要post的数据
    html = sess.get("https://leetcode-cn.com/accounts/login/",headers=headers).text


if __name__ =="__main__":
    leetcodeLogin()
