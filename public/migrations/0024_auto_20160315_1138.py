# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 08:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0023_auto_20160315_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 15, 11, 38, 15, 626624), verbose_name='Дата публикации'),
        ),
        migrations.AlterModelTable(
            name='comments',
            table='comments',
        ),
    ]