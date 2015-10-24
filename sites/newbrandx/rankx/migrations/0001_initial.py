# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=400)),
                ('startup', models.DateField(verbose_name=b'company founded')),
                ('scale', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Milk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=0)),
                ('pv', models.IntegerField(default=0)),
                ('taobao_sales', models.IntegerField(default=0)),
                ('jd_sales', models.IntegerField(default=0)),
                ('tmall_sales', models.IntegerField(default=0)),
                ('vip_sales', models.IntegerField(default=0)),
                ('amazon_sales', models.IntegerField(default=0)),
                ('weibo_fans', models.IntegerField(default=0)),
                ('weibo_forward', models.IntegerField(default=0)),
                ('weixin_fans', models.IntegerField(default=0)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('brand_name', models.ForeignKey(related_name='brand_name', to='rankx.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.ForeignKey(related_name='company_name', to='rankx.Company'),
        ),
    ]
