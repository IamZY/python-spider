# -*- coding: utf-8 -*-
import scrapy

# 只需要提供post数据的模拟登录
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = [
        'http://renren.com/'
    ]

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        yield scrapy.FormRequest(
            url = url,
            formdata={
                "email":"18602541089",
                "password":"zangyang951026",
            },
            callback=self.parse_page
        )


    def parse_page(self,response):
        with open("index.html","w") as file:
            file.write(response.body)
