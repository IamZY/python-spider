# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs


class douyu(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.num = 0
    # 测试方法 以test开头 test..()
    def testOuoyu(self):
        self.driver.get("https://www.douyu.com/directory/all")

        while True:
            soup = bs(self.driver.page_source, "lxml")
            names = soup.find_all("h3", {"class": "ellipsis"})
            numbers = soup.find_all("span", {"class": "dy-num fr"})
            # 合并成元组
            for name, number in zip(names, numbers):
                print u"观众人数:" + number.get_text().strip() + u"\t房间名:" + name.get_text().strip()
                self.num += 1

            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                break;

            self.driver.find_element_by_class_name("shark-pager-next").click()

    def tearDown(self):
        # 退出PhantomJS
        print self.num
        self.driver.quit()


if __name__ == "__main__":
    # 启动测试模块
    unittest.main()
