# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
import sys
sys.path.append("..")
# from ..settings import USER_AGENTS
# from settings import PROXIES
from .settings import USER_AGENTS
from .settings import PROXIES


# 随机User-Agent
class RandomUserAgent(object):
    def process_request(self,request,spider):
        userAgent = random.choice(USER_AGENTS)
        # 重新设置消息头
        request.headers.setdefault("User-Agent",userAgent)

# 代理信令
class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)

        if proxy["user_password"] is None:
            # 如果没有代理账户验证的代理使用
            request.meta["proxy"] = "http://" + proxy["ip_port"]
        else:
            # 需要经过base64进行转码
            base64_user_password = base64.b64encode(proxy["user_password"])
            # 对账户密码进行base64密码转换
            request.meta["proxy"] = "http://" + proxy["ip_port"]
            # 对应代理服务器的信令
            request.headers["Proxy_Authorization"] = "Basic " + base64_user_password