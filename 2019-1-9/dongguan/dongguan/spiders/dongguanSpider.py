# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DongguanItem

class DongguanspiderSpider(CrawlSpider):
    name = 'dongguanSpider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = [
        'http://wz.sun0769.com/index.php/question/report?page=0'
    ]


    rules = (
        # 匹配问号后面的
        Rule(LinkExtractor(allow=r'page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback="parse_item")
    )

    def parse_item(self,response):
        item = DongguanItem()
        item['title'] = response.xpath('//div[@class="wzy1"]//td[2]/span[1]/text()').extract()[0].split(": ")[-1]
        item['content'] = response.xpath('//div[@class="wzy1"]//table[2]//tr[1]/td[@class="txt16_3"]/text()').extract()[0]
        item['url'] = response.url
        item['number'] = response.xpath('//div[@class="wzy1"]//td[2]/span[2]/text()').extract()[0].split(":")[-1]

        yield item
