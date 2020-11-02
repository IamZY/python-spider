# -*- coding: utf-8 -*-
import scrapy
import selenium
import time
from ..items import QichachaItem
from ..settings import DEFAULT_REQUEST_HEADERS
from ..settings import USER_AGENTS
import random

class QccSpider(scrapy.Spider):
    name = 'qcc'
    allowed_domains = ['www.qichacha.com']

    offset = 1
    url = "https://www.qichacha.com/gongsi_area.shtml?prov=JS&city=320100&p="
    start_urls = [
        url + str(offset)
    ]

    print("+++++++++++++" + random.choice(USER_AGENTS))
    # 2、生成当前时间戳
    now_time = int(time.time())

    print("====================="+str(now_time))

    first_url='https://www.qichacha.com'

    cookies = {
                  "UM_distinctid": "16bd4a9ac6d45d-0676947eb3db168-4c312d7d-144000-16bd4a9ac6e123",
                  "CNZZDATA1254842228": "2024856680-1562636084-https%253A%252F%252Fwww.baidu.com%252F%7C1563844707",
                  "zg_did": "%7B%22did%22%3A%20%2216bd4a9ad83173-0d01db6c216bd4-4c312d7d-144000-16bd4a9ad8435f%22%7D",
                  "zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f": "%7B%22sid%22%3A%201563843529553%2C%22updated%22%3A%201563846518592%2C%22info%22%3A%201563759307615%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22c52cb965b148b68a57da9d5f61d9ba3c%22%7D",
                  "Hm_lvt_3456bee468c83cc63fb5147f119f1075": "1563780086,1563780714,1563783273,1563843530",
                  "_uab_collina": "156264101867396590751684",
                  "acw_tc": "755bb21f15626410184594689e158a3142c18747c20e27765a308d7679",
                  "QCCSESSID": "44mn7dvgcmamd7hqcg2ghsbh57",
                  "Hm_lpvt_3456bee468c83cc63fb5147f119f1075": str(now_time),
                  "acw_sc__v3": "5d3665adf10969301930ac3f6860f507ebcb73df",
                  "acw_sc__v2": "5d3665adedf94c5248326568f12ec8881686a3a3"
              }


    def start_requests(self):
        yield scrapy.Request(
            url=self.url + str(self.offset),
            # headers=random.choice(USER_AGENTS),
            cookies=self.cookies,
            callback=self.parse
        )

    def parse(self, response):
        # print(response.body)
        # loginUrlloginUrl = 'https://www.qichacha.com/user_login'
        time.sleep(2)
        ret = response.xpath("//table[@class='m_srchList']//tr")
        index = 0
        for r in ret:
            item = QichachaItem()
            href = r.xpath("//a[@class='ma_h1']/@href").extract()[index]
            item["businessPerson"] = r.xpath("//a[@class='a-blue']/text()").extract()[index]
            item["phoneNumber"] = r.xpath("//p[2]/span[@class='m-l']/text()").extract()[index]
            # print(href)
            # item["businessName"] = r.xpath("//a[@class='ma_h1']/text()").extract_first()
            # item["businessPerson"] = r.xpath("//a[@class='a-blue']/text()").extract_first()
            # item["phoneNumber"] = r.xpath("//a[@class='a-blue']/text()").extract_first()
            # print(href)
            yield scrapy.Request(
                self.first_url + str(href),
                # headers=random.choice(USER_AGENTS),
                cookies=self.cookies,
                callback=self.parse_detail,
                meta={"item": item}
            )
            index+=1

        if self.offset < 500:
            self.offset += 1

        yield scrapy.Request(
            url=self.url + str(self.offset),
            # headers=random.choice(USER_AGENTS),
            cookies=self.cookies,
            callback=self.parse
        )

    def parse_detail(self,response):
        item = response.meta["item"]
        item["businessName"] = response.xpath("//div[@class='content']/div[1]/h1/text()").extract_first()
        print(item)
        yield item
