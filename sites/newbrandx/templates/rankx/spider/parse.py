#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: jackytu<zhongying.tu@gmail.com>
import json
import chardet
import re

fd = open('data')
s = json.load(fd)

number = re.compile('[0-9]+')

for i in s["mods"]["itemlist"]["data"]["auctions"]:
    sales_number = i['view_sales']
    print number.findall(sales_number)[0]
