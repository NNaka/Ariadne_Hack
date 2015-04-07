# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirth', '0004_auto_20150214_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='baby_height_cm',
        ),
        migrations.AddField(
            model_name='baby',
            name='baby_height',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='baby',
            name='baby_weight',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='baby_gender',
            field=models.CharField(default=b'other', help_text=b'Gender of baby', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female'), (b'other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='baby_health',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='birth_datetime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='birth_of_baby',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baby',
            name='conception_datetime',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mother',
            name='age',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mother',
            name='first_name',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mother',
            name='last_name',
            field=models.CharField(default=b'', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mother',
            name='mother_condition',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
