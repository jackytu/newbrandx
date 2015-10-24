# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankx', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brand'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Company'},
        ),
        migrations.AlterModelOptions(
            name='milk',
            options={'verbose_name': 'Milk', 'verbose_name_plural': 'Milk'},
        ),
        migrations.AddField(
            model_name='milk',
            name='brand_record',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
