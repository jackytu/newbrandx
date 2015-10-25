#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import MySQLdb
import datetime

brand_data = {}

today = datetime.date.today()
report_tittle = "milk/milk_best.html"

first = today.replace(day=1)
last_year = first - datetime.timedelta(days=365)
rang_low = last_year.strftime("%Y-%m-01")
rang_high = today.strftime("%Y-%m-01")
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
         "rankx_best.year",
         "from rankx_best",
         "left join rankx_brand",
         "on rankx_best.winner_id = rankx_brand.id"
         ]

sql_query = " ".join(query)

results = cur.execute(sql_query)

info = cur.fetchmany(results)

sort1 = sorted(info, key=lambda d:d[1], reverse = True)

report = open(report_tittle, 'w')
content = '''
<div class = "row">
<table class = "table table-hover">
'''
content += '<tr><td>年份</td><td>最佳品牌</td></tr>'

for brand, year in sort1:
    content += '''
    <tr><td>{}</td><td>{}</td></tr>
    '''.format(year, brand)

content += '''
</table>
</div>
'''
report.write(content)
report.close()


