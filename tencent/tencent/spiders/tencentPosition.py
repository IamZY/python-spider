# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?keywords=&lid=0&start='

    offset = 0

    start_urls = [
        url + str(offset)
    ]


    def parse(self, response):

        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentItem()

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

            # 将数据发送到管道文件
            yield item

        if self.offset < 2830:
            self.offset += 10

        # 每次处理完一页的数据之后 重新发送新的页的页面请求 offset自增10
        # 同时拼接新的url 并且用回调函数
        # 将请求重新发送给调度器
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
