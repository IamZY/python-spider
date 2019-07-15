import scrapy

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 处理start_url地址对应的相应
        ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        print(ret1)