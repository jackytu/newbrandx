#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import MySQLdb
import datetime
import time

brand_data = {}

today = datetime.date.today()
report_tittle = "milk/milk_{}.json".format(today.strftime("%Y_%m"))

first = today.replace(day=1)
last_year = first - datetime.timedelta(days=2*365)
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

query = ["select rankx_milk.pub_date,",
        "rankx_milk.rank,",
        "rankx_brand.name",
        "from rankx_milk",
        "left join rankx_brand",
        "on rankx_milk.brand_name_id = rankx_brand.id",
         ]

sql_query = " ".join(query)

results = cur.execute(sql_query)

info = cur.fetchmany(results)
cur.close()
conn.commit()
conn.close()

pub_date_list = []
pub_date_dict = {}

for ii in info:
    (pub_date_raw, rank, brand_raw) = ii
    pub_date = pub_date_raw.strftime("%Y-%m")
    pub_date_utc = int(time.mktime(pub_date_raw.timetuple()))
    brand = brand_raw.replace(" ", "")
    if not pub_date_utc in pub_date_dict:
        pub_date_dict[pub_date_utc] = pub_date

    if not brand in brand_data:
        brand_data[brand] = {}
    brand_data[brand][pub_date] = rank

output_data = {}
pub_date_dict_sort = sorted(pub_date_dict.items(), key=lambda e:e[0], reverse = False)
for (utc, timestamp) in pub_date_dict_sort:
    pub_date_list.append(timestamp)

output_data['x-aris'] = pub_date_list
output_data['chart_data'] = []

print brand_data


for brand, data in brand_data.items():
    meta = {}
    meta['name'] = brand
    meta['value'] = []

    for date in pub_date_list:
        meta['value'].append(data[date])

    output_data['chart_data'].append(meta)

print output_data

chart_json = open(report_tittle, 'w')
chart_json.write(json.dumps(output_data))
chart_json.close()







