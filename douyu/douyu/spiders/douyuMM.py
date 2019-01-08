# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

class DouyummSpider(scrapy.Spider):
    name = 'douyuMM'
    allowed_domains = ['www.douyu.com']

    url = "https://www.douyu.com/gapi/rknc/directory/yzRec/"

    offset = 0

    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        # json转python
        # 取出来的是一个列表
        data = json.loads(response.text)["data"]
        rl = data["rl"]

        for each in rl:
            item = DouyuItem()
            item["name"] = each["nn"]
            item["imageLink"] = each["rs16"]

            yield item

        if self.offset < 10:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)