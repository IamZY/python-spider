# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
from ..items import ZhihuItem

class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    # http不可以写
    allowed_domains = ['www.zhihu.com']

    start_urls = [
        "https://www.zhihu.com/api/v4/questions/56378769/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=5&offset=0&platform=desktop&sort_by=default"
    ]

    def parse(self, response):
        # pass
        # response
        data_list = json.loads(response.text)["data"]

        nextPage = json.loads(response.text)["paging"]

        for each in data_list:
            item = ZhihuItem()
            item["author"] = each["author"]["name"]
            content = each["content"]

            html = etree.HTML(content)

            # etree.HTML

            image_list = html.xpath('//figure/img/@data-original')
            item["imageLink"] = image_list

            yield item


        if not nextPage["is_end"]:
            # dont_filter 忽略域组的范围
            # yield scrapy.Request(nextPage["next"],callback=self.parse,dont_filter=True)
            yield scrapy.Request(nextPage["next"],callback=self.parse)