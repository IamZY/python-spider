# -*- coding: utf-8 -*-

import scrapy
# 导入CrawlSpider父类和Rule父类
from scrapy.spiders import CrawlSpider,Rule
# 提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from ..items import TencentspiderItem


class TencentSpider(CrawlSpider):
    name = "tencent"
    allowed_domains = ['tencent.com']

    start_urls = [
        "https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start=0#a"
    ]

    # Response 连接的提取规则 返回符合匹配规则的连接匹配对象的列表
    pageLink = LinkExtractor(allow=("start=\d+"))
    # newLink = LinkExtractor(allow=('position.php?'))

    # 匹配规则
    # 可以匹配多个规则信息
    rules = [
        # follow跟进连接
        # 获取这个列表中的连接 依次发送请求 一次跟进 调用指定的回调函数处理
        Rule(pageLink,callback="parseTencent",follow=True),
        # Rule(newLink,callback="")
    ]

    # 指定的回调函数
    def parseTencent(self,response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentspiderItem()
            # 职位名
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详细连接
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

