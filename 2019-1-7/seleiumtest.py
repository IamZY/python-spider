# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://www.douban.com/")

driver.find_element_by_name("form_email").send_keys("*********")

driver.find_element_by_name("form_password").send_keys("*********")

driver.find_element_by_class_name("bn-submit").click()

driver.save_screenshot("douban.png")
