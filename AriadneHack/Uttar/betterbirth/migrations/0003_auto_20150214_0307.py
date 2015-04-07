# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirth', '0002_auto_20150214_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='postal_code',
            field=models.CharField(default=b'0000-000', max_length=8),
            preserve_default=True,
        ),
    ]
