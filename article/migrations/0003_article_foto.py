# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='foto',
            field=models.ImageField(default=datetime.datetime(2016, 2, 27, 18, 30, 44, 910000, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
