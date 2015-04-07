# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirth', '0005_auto_20150214_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='mother',
            name='home_city',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='birth_datetime',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='conception_datetime',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
