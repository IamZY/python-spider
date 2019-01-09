# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import os
import time

class ZhiHuImagesPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        for each in item["imageLink"]:
            yield scrapy.Request(each)

    def item_completed(self, results, item, info):
        # 图片原来的名字
        image_path = [x["path"] for ok, x in results if ok]

        # os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + image_path[0] + ".jpg")

        # item["imagePath"] = self.IMAGES_STORE + "/" + image_path[0]

        item["imagePath"] = image_path


        return item


