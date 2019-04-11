#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
from lxml import etree
# 导入pymysql模块
import pymysql
# 打开一个数据库连接
db = pymysql.connect(host='127.0.0.1', user='zhaoxin', password='1989zx', port=3306, db='world', use_unicode=True, charset="utf8")
# 获取MySQL的操作游标，利用游标来执行SQL语句
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS employee")
sql = """CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
cursor.execute(sql)
print("Created table Successfull.")
db.close()


headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
url = 'http://maoyan.com/board/4'
response = requests.get(url, headers=headers)
html = response.text
html = etree.HTML(html)
result_bawangbieji = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a')
print(result_bawangbieji[0].text)
result_all = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
print('该页面全部电影名：')
for one in result_all:
 print(one.text)
