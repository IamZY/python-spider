# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['movie.douban.com']

    url = "https://movie.douban.com/top250?start="

    offset = 0

    start_urls = [
        url + str(offset)
    ]


    def parse(self, response):
        # pass
        for each in response.xpath('//div[@class="info"]'):
            item = DoubanItem()
            item["title"] = each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            item["bd"] = each.xpath('.//div[@class="bd"]/p[1]/text()[1]').extract()[0].strip() \
                         + each.xpath('.//div[@class="bd"]/p[1]/text()[2]').extract()[0]
            item["star"] = each.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            if len(each.xpath('.//span[@class="inq"]/text()').extract()) == 0:
                item["quote"] = "none"
            else:
                item["quote"] = each.xpath('.//span[@class="inq"]/text()').extract()[0]

            yield item

        if self.offset < 225:
            self.offset += 25

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)