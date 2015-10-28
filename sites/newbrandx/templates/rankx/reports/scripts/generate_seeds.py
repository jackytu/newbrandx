#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import datetime
import random

brand_data = {}

today = datetime.date.today()
report_tittle = "milk/milk_{}.html".format(today.strftime("%Y_%m"))

first = today.replace(day=1)
last_year = first - datetime.timedelta(days=365)
rang_low =  today.strftime("%Y-01-01")
rang_high = today.strftime("%Y-12-31")
this_year = today.year

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='br',
        passwd='123456',
        db ='brandrank',
        )
cur = conn.cursor()

query = ["select",
         "name,",
         "id",
         "from rankx_brand"
         ]

sql_query = " ".join(query)
print sql_query

results = cur.execute(sql_query)

info = cur.fetchmany(results)

sql_template = "insert into rankx_milk (rank, pv,taobao_sales,jd_sales,tmall_sales,vip_sales,amazon_sales,weibo_fans,weibo_forward, weixin_fans,pub_date, brand_name_id, brand_record) values"
pub_dates = []
for d in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
    for y in ['2013', '2014', '2015']:
        pub_dates.append('{}-{}-02'.format(y, d))

for name, bid in info:
    for d in pub_dates:
        pv = 10000 + random.randint(1, 10000)
        taobao_sales = 20000 + random.randint(1, 10000)
        jd_sales = 20000 + random.randint(1, 10000)
        tmall_sales = 20000 + random.randint(1, 10000)
        vip_sales = 20000 + random.randint(1, 10000)
        amazon_sales = 20000 + random.randint(1, 10000)
        weibo_fans = 20000 + random.randint(1, 10000)
        weibo_forward = 20000 + random.randint(1, 10000)
        weixin_fans = 20000 + random.randint(1, 10000)
        brand_record = name.replace(' ', '_').replace('-', '_') + '_' + d.replace('-', '_')
        sql = sql_template + "(0, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}', {}, '{}');".format(
                pv, taobao_sales, jd_sales, tmall_sales, vip_sales, amazon_sales, weibo_fans,
                weibo_forward, weixin_fans, d, bid, brand_record
                )
        print sql
        cur.execute(sql)

cur.close()
conn.commit()
conn.close()
