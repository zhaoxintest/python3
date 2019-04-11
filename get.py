#!/usr/bin/python3
# -*- coding:utf-8 -*-

import requests

url = 'https://www.baidu.com'
r = requests.get(url,verify=False)
print(r.status_code)
print(r.request)
print(r.text)
