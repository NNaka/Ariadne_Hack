# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mother',
            name='geo_loc',
        ),
        migrations.AddField(
            model_name='mother',
            name='postal_code',
            field=models.CharField(default=b'0000-000', max_length=7),
            preserve_default=True,
        ),
    ]
