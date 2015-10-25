# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankx', '0002_auto_20151024_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milk',
            old_name='index',
            new_name='rank',
        ),
    ]
