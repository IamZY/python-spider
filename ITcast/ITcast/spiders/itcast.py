# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print(response.body)
        # pass
        # //div[@class='main_bot']
        nodes = response.xpath("//div[@class='tea_box4 box_teacher ']//li")
        # items = []
        for n in nodes:
            name = n.xpath("./div[@class='main_bot']/h2/text()").extract()
            title = n.xpath("./div[@class='main_bot']/h2/span/text()").extract()
            print(name[0])
            print(title[0])
            itcast = ItcastItem()
            itcast['name'] = name[0]
            itcast['title'] = title[0]
            itcast['info'] = ' '
            # 返回提取到的没个item数据 给管道文件处理 同时还回来继续执行后面的代码
            yield itcast
            # items.append(itcast)
        # return items