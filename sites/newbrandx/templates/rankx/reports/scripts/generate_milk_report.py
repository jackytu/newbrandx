#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime

brand_data = {}

today = datetime.date.today()
report_tittle = "milk/milk_{}.html".format(today.strftime("%Y_%m"))

first = today.replace(day=1)
last_year = first - datetime.timedelta(days=365)
rang_low = last_year.strftime("%Y-%m-01")
rang_high = today.strftime("%Y-%m-28")
month_high = today.strftime("%Y_%m")
month_low = last_year.strftime("%Y_%m")
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='br',
        passwd='123456',
        db ='brandrank',
        )
cur = conn.cursor()

query = ["select rankx_brand.name, rankx_milk.index, rankx_milk.pub_date from rankx_milk",
         "left join rankx_brand",
         "on rankx_milk.brand_name_id = rankx_brand.id",
         "where rankx_milk.pub_date >",
         "'{}'".format(rang_low),
         "and rankx_milk.pub_date <",
         "'{}'".format(rang_high),
         ]

sql_query = " ".join(query)

results = cur.execute(sql_query)

info = cur.fetchmany(results)
cur.close()
conn.commit()
conn.close()

for ii in info:
    (brand_raw, index, pub_date) = ii
    brand = brand_raw.replace(' ', '')
    if not brand_data.has_key(brand):
        brand_data[brand] = {}
        brand_data[brand]['brand'] = brand
    year = pub_date.year
    this_year = datetime.date.today().year

    if year == this_year:
        brand_data[brand]['this_year'] = index
    else:
        brand_data[brand]['last_year'] = index

for (brand, data) in brand_data.items():
    if data['this_year'] >= data['last_year']:
        data['trend'] = 'up'
    else:
        data['trend'] = 'down'

    if data['last_year'] != 0:
        rating = abs((float(data['this_year']) - float(data['last_year']))/float(data['last_year']) * 100)
    else:
        rating = 100
    data['rating'] = rating

report = open(report_tittle, 'w')
content = '''
<div class = "row">
<table class = "table table-hover">
'''
content += '<tr><td>{}</td><td>{}</td><td>趋势</td><td>品牌</td><td>得分</td><td>变化率</td></tr>'.format(month_high, month_low)

for (brand, data) in brand_data.items():
    content += '''
    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>90</td><td>{}</td></tr>
    '''.format(data['this_year'], data['last_year'], data['trend'], brand, data['rating'])
content += '''
</table>
</div>
'''
report.write(content)
report.close()


