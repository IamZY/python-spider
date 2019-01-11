# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql
from scrapy.conf import settings


class DoubanPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWD"],
            charset='utf8',
            use_unicode=True
        )

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 插入数据
        self.cursor.execute(
            """insert into doubanmovies(title, bd, star , quote) value( %s, %s, %s, %s) """,
            (item['title'],
             item['bd'],
             item['star'],
             item['quote'],
             )
        )
        # 提交sql语句
        self.connect.commit()


    # def __init__(self):
    #     host = settings["MONGODB_HOST"]
    #     port = settings["MONGODB_PORT"]
    #     dbname = settings["MONGODB_DBNAME"]
    #     sheetname = settings["MONGODB_SHEETNAME"]
    #
    #     # 创建mongodb的数据库连接
    #     client = pymongo.MongoClient(host=host,port=port)
    #     # 指定数据库
    #     mydb = client[dbname]
    #     # 指定存放数据库的数据库表名
    #     self.mysheet = mydb[sheetname]
    #
    # def process_item(self, item, spider):
    #
    #     data = dict(item)
    #
    #     # . .insert(data)
    #
    #     self.mysheet.insert(data)
    #
    #     return item
