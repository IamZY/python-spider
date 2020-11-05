# python-spider
+ 知乎+腾讯招聘+斗鱼+豆瓣爬虫

## Spider

+ 流程图

![image](D:\src\python-spider\Image\1.png)

+ 创建爬虫

  scrapy startproject myspider

  scrapy genspider 爬虫名 "网址"

+ 执行爬虫

  scrapy crawl 爬虫名 -o xxx.json/csv

+ scrapy shell

# 备注

+ yangguang 爬取链接 并通过链接再次进入爬取
+ douyu 爬取图片 json格式链接
+ 需要在`settings.py`启用管道文件