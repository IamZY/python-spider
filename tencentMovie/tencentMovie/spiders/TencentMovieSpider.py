# -*- coding: utf-8 -*-
import scrapy

from ..items import TencentmovieItem

class TencentmoviespiderSpider(scrapy.Spider):
    name = 'TencentMovieSpider'
    allowed_domains = ['v.qq.com']

    url = "http://v.qq.com/x/list/movie?iarea=-1&subtype=-1&offset="

    offset = 0

    start_urls = [
        url + str(offset)
    ]

    def parse(self, response):
        for each in response.xpath('//li[@class="list_item"]'):

            item = TencentmovieItem()
            item["movieName"] = each.xpath('./div[@class="figure_title_score"]/strong/a/@title').extract()[0]
            item["imagePath"] = each.xpath('./a[@class="figure"]/img/@src').extract()[0]
            print item["movieName"]
            print item["imagePath"]
            yield item

        if self.offset < 4980:
            self.offset += 30

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)