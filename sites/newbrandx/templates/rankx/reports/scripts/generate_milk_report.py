#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import datetime

brand_data = {}

today = datetime.date.today()
report_tittle = "milk/milk_{}.html".format(today.strftime("%Y_%m"))

first = today.replace(day=1)
last_year = first - datetime.timedelta(days=365)
rang_low = last_year.strftime("%Y-%m-02")
rang_high = today.strftime("%Y-%m-02")
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

query = ["select",
         "rankx_brand.name,",
         "rankx_milk.brand_name_id,",
         "rankx_milk.rank,",
         "rankx_milk.pv,",
         "rankx_milk.taobao_sales,",
         "rankx_milk.jd_sales,",
         "rankx_milk.tmall_sales,",
         "rankx_milk.vip_sales,",
         "rankx_milk.amazon_sales,",
         "rankx_milk.weibo_fans,",
         "rankx_milk.weibo_forward,",
         "rankx_milk.weixin_fans,",
         "rankx_milk.pub_date",
         "from rankx_milk",
         "left join rankx_brand",
         "on rankx_milk.brand_name_id = rankx_brand.id",
         "where rankx_milk.pub_date =",
         "'{}'".format(rang_low),
         "or rankx_milk.pub_date =",
         "'{}'".format(rang_high),
         ]

sql_query = " ".join(query)

results = cur.execute(sql_query)

info = cur.fetchmany(results)

for ii in info:
    (brand_raw, brand_id, rank_raw, pv, taobao_sales, jd_sales,
        tmall_sales, vip_sales, amazon_sales,
        weibo_fans, weibo_forward, weixin_fans, pub_date) = ii
    brand = brand_raw.replace(' ', '')
    if not brand_data.has_key(brand):
        brand_data[brand] = {}
        brand_data[brand]['brand'] = brand
    year = pub_date.year
    this_year = datetime.date.today().year

    rank = (pv * 0.2 + (taobao_sales + jd_sales + tmall_sales + vip_sales + amazon_sales)*0.6 + (weibo_fans + weibo_forward + weixin_fans)*0.2)

    if year == this_year:
        brand_data[brand]['this_year'] = rank
    else:
        brand_data[brand]['last_year'] = rank

    sql = "update rankx_milk set rank = {} where brand_name_id = {} and pub_date = '{}'".format(rank, brand_id, pub_date)
    print sql
    cur.execute(sql)

print brand_data

cur.close()
conn.commit()
conn.close()

for (brand, data) in brand_data.items():
    if data['this_year'] > data['last_year']:
        data['trend'] = "<img src='static/demo/img/ui/down.png'></img>"
    elif data['this_year'] == data['last_year']:
        data['trend'] = '-'
    else:
        data['trend'] = "<img src='static/demo/img/ui/upup.png'></img>"

    if data['last_year'] != 0:
        rating = abs((float(data['this_year']) - float(data['last_year']))/float(data['last_year']) * 100)
    else:
        rating = 100
    data['rating'] = rating

sort1 = sorted(brand_data.iteritems(), key=lambda d:d[1]['last_year'], reverse = False)
brand_lyear = {}
idx = 1
for brand, data in sort1:
    brand_lyear[brand] = idx
    idx += 1

sort2 = sorted(brand_data.iteritems(), key=lambda d:d[1]['this_year'], reverse = False)

report = open(report_tittle, 'w')
content = '''
<div class = "row">
<table class = "table table-hover">
'''
content += '<tr><td>{}</td><td>{}</td><td>趋势</td><td>品牌</td><td>得分</td><td>变化率</td></tr>'.format(month_high, month_low)

idx2 = 1
for brand, data in sort2:
    content += '''
    <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>
    '''.format(idx2, brand_lyear[brand], data['trend'], brand, data['this_year'], data['rating'])
    idx2 += 1
content += '''
</table>
</div>
'''
report.write(content)
report.close()


