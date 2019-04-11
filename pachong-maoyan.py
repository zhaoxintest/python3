#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import time
from lxml import etree
# 导入CSV模块
import csv
# 导入pymysql模块
# import pymysql
# # 打开一个数据库连接
# db = pymysql.connect(host='127.0.0.1', user='zhaoxin', password='1989zx', port=3306, db='world', use_unicode=True, charset="utf8")
# # 获取MySQL的操作游标，利用游标来执行SQL语句
# cursor = db.cursor()

headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://maoyan.com/board/4'
response = requests.get(url,headers=headers)
html = response.text
# 调用HTML类进行初始化
html = etree.HTML(html)
# 粘贴我们copy的xpath，提取电影名 “霸王别姬”
result_bawangbieji = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a')
#　打印节点标签包含的文本内容
print(result_bawangbieji[0].text)
# 提取该页面所有电影名，即选择所有'dd'标签的电影名
result_all = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
#　打印所有提取出的电影名
print('该页面全部电影名：')
for one in result_all:
    print(one.text)
    # try:
    #     # 插入数据语句
    #     sql = 'INSERT INTO film_infor(name) values (%s)'
    #     cursor.execute(sql, (one.text))
    #     db.commit()
    # except:
    #     db.rollback()
    # db.close()

# 将这一页电影名存储至TEXT文件中，'a' 指打开一个文件进行追加。 如果文件存在，则文件指针位于文件末尾。也就是说，文件处于追加模式。如果文件不存在，它将创建一个新文件进行写入。

with open('film_name.txt','w+') as f:
    for one in result_all:
        f.write(one.text  + '\n')
    f.close()

# 将这一页电影名存储至CSV文件中：
with open('film_name.csv', 'w+', newline='') as f:
    csv_file = csv.writer(f)
    for one in result_all:
        csv_file.writerow([one.text])

