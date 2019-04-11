#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import requests

# 一定要设置Content-Type值为application/json
headers = {}
headers['Content-Type'] = 'application/json'

url = 'https://www.baidu.com'
data = {"username":"ls","password":"toor"}
# 一定要用json.dumps把data格式化成json
# r = requests.post(url,headers=headers,data=json.dumps(data),verify=False)
# 或者直接使用json参数代替data，此时requests会自动进行格式化和设置Content-Type头的工作
r = requests.post(url,json=data,verify=False)
print(r.status_code)
print(r.request)
print(r)