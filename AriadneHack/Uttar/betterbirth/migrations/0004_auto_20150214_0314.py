# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betterbirth', '0003_auto_20150214_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baby',
            old_name='baby_height',
            new_name='baby_height_cm',
        ),
    ]
