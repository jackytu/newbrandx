# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankx', '0003_auto_20151025_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=1900)),
                ('winner', models.ForeignKey(related_name='best_brand_name', to='rankx.Brand')),
            ],
        ),
    ]
