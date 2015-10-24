# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('startup', models.DateTimeField(verbose_name=b'company founded')),
                ('scale', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MilkIndex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=200)),
                ('index', models.IntegerField(default=0)),
                ('pv', models.IntegerField(default=0)),
                ('sales', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
