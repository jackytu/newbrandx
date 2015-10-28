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
         "id,",
         "rank,",
         "pv,",
         "taobao_sales,",
         "jd_sales,",
         "tmall_sales,",
         "vip_sales,",
         "amazon_sales,",
         "weibo_fans,",
         "weibo_forward,",
         "weixin_fans",
         "from rankx_milk"
         ]

sql_query = " ".join(query)

results = cur.execute(sql_query)

info = cur.fetchmany(results)

for ii in info:
    (record_id, rank_raw, pv, taobao_sales, jd_sales,
        tmall_sales, vip_sales, amazon_sales,
        weibo_fans, weibo_forward, weixin_fans) = ii

    rank = (pv * 0.2 + (taobao_sales + jd_sales + tmall_sales + vip_sales + amazon_sales)*0.6 + (weibo_fans + weibo_forward + weixin_fans)*0.2)

    sql = "update rankx_milk set rank = {} where id={}".format(rank, record_id)
    print sql
    cur.execute(sql)


cur.close()
conn.commit()
conn.close()
