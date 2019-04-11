#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests

response = requests.get('https://gitbook.cn')

print(response.status_code)

data = {"name":"zhaoxin","age":"30"}

response1 = requests.post("https://httpbin.org/post",data=data)

print(response1.text)