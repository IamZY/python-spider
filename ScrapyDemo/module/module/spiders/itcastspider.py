# -*- coding:utf-8 -*-

import scrapy
from ..items import ItcastItems

# 创建爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫真实的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]


    def parse(self, response):
        # with open("teacher.html","w") as f:
        #     f.write(response.body)

        # response.xpath('//div[@class="li_txt"]')
        # response.xpath('./h3/text())
        teacher_list = response.xpath('//div[@class="li_txt"]')

        TeacherItem = []

        for each in teacher_list:

            item = ItcastItems()

            # 把匹配的对象转换成unicode字符串
            # 不加extract() 就是匹配过后的对象
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            # print name[0]
            # print title[0]
            # print info[0]
            item["name"] = name[0].replace(u'\xa0', u' ')
            item["title"] = title[0].replace(u'\xa0', u' ')
            item["info"] = info[0].replace(u'\xa0', u' ')

            TeacherItem.append(item)

        return TeacherItem