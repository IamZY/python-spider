# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentjobItem
import json

class TencentjobspiderSpider(scrapy.Spider):
    name = 'tencentjobspider'
    allowed_domains = ['tencent.com']

    # https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1604491999741&pageIndex=1&pageSize=10
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1604491999741&pageSize=10&pageIndex="

    offset = 1

    start_urls = [
        base_url + str(offset)
    ]

    def parse(self, response):
        data = json.loads(response.text)['Data']
        jobs = data["Posts"]

        for item in jobs:
            class_ = TencentjobItem()
            class_['jobName'] = item['RecruitPostName']
            class_['jobCity'] = item['LocationName']
            print(class_['jobName'] + "-----" +  class_['jobCity'])

        if self.offset < 10:
            self.offset += 1

        yield scrapy.Request(self.base_url + str(self.offset),callback=self.parse)
