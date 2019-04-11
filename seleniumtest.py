# -*- coding:utf-8 -*-

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(200)
driver.quit()