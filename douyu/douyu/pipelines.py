# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 获取项目文件中的内容
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

class DouyuPipeline(ImagesPipeline):
    # 获取settings文件中的值

    print "==============================================="

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        print "------------------------------------------------------"
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 图片原来的名字
        image_path = [x["path"] for ok , x in results if ok]

        os.rename(self.IMAGES_STORE + "/" + image_path[0],self.IMAGES_STORE + "/" + item["name"] + ".jpg")

        item["imagePath"] = self.IMAGES_STORE + "/" + item["name"]

        return item