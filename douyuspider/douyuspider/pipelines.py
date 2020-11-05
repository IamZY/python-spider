# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os


class DouyuspiderPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item['pic']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 提取results中的路径
        # [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/roomCover/2020/07/31/5ec1cda757678fff6bb7e007406c9022_big.jpg/dy1', 'path': 'full/13ac01be7de198fa5122e881dc84195371e8405e.jpg', 'ch
        # ecksum': '09a9aed4e5904b7d7737d73d8f5beb82'})]
        # print(results)

        # ok代表results前面的 True x 代表除了True后面的
        path = [x['path'] for ok, x in results if ok]

        os.rename(self.IMAGES_STORE + path[0], self.IMAGES_STORE + item['name'] + '.jpg')

        return item
