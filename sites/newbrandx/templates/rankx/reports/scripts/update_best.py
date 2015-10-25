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
         "rankx_brand.name,",
         "rankx_milk.brand_name_id,",
         "rankx_milk.rank",
         "from rankx_milk",
         "left join rankx_brand",
         "on rankx_milk.brand_name_id = rankx_brand.id",
         "where rankx_milk.pub_date >",
         "'{}'".format(rang_low),
         "and rankx_milk.pub_date <",
         "'{}'".format(rang_high),
         ]

sql_query = " ".join(query)
print sql_query

results = cur.execute(sql_query)

info = cur.fetchmany(results)

for ii in info:
    (brand_raw, brand_id, rank_raw) = ii
    brand = brand_raw.replace(' ', '')
    if not brand_data.has_key(brand):
        brand_data[brand] = {}
        brand_data[brand]['rank'] = 0
        brand_data[brand]['id'] = brand_id
    brand_data[brand]['rank'] += rank_raw

print brand_data

sort1 = sorted(brand_data.iteritems(), key=lambda d:d[1]['rank'], reverse = True)
best_brand, rank = sort1[0]
print sort1
sql = "insert into rankx_best (year, winner_id) values ({}, {});".format(this_year, rank['id'])

print sql
cur.execute(sql)

cur.close()
conn.commit()
conn.close()
