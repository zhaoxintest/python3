#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests

url = 'https://www.baidu.com'
data="username=ls&password=toor"
r = requests.post(url,data=data,verify=False)
print(r.status_code)
print(r.request)
print(r.text)