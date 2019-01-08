# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ItcastPipeline(object):
    # 可选的作为类的初始化方法
    def __init__(self):
        # 创建了一个文件
        self.filename = open("teacher.json","w")
    # 处理item数据 这个方法是必须写的
    def process_item(self,item,spider):
        jsontext = json.dumps(dict(item),ensure_ascii = False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item

    # 可选的 执行结束后
    def close_spider(self):
        self.filename.close()

    # def process_item(self, item, spider):
        # return item
