# -*- coding: utf-8 -*-
import scrapy
from ..items import DouyuspiderItem

import json

class DyspiderSpider(scrapy.Spider):
    name = 'dyspider'
    allowed_domains = ['www.douyu.com']

    # base_url = 'http://www.douyu.com/gapi/rkc/directory/mixList/2_1008/'
    base_url = 'https://www.douyu.com/gapi/rknc/directory/yzRec/'

    offset = 1

    start_urls = [
        base_url + str(offset)
    ]

    def parse(self, response):
        data_list = json.loads(response.text)['data']['rl']

        if len(data_list) == 0:
            return

        for item in data_list:
            douyu = DouyuspiderItem()
            douyu['name'] = item['nn']
            douyu['pic'] = item['rs16']
            yield douyu

        self.offset += 1
        yield scrapy.Request(self.base_url + str(self.offset),callback=self.parse)
