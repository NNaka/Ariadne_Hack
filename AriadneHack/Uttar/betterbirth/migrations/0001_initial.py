# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baby_gender', models.CharField(default=b'text', help_text=b'Gender of baby', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female'), (b'other', b'Other')])),
                ('conception_datetime', models.DateTimeField(auto_now_add=True)),
                ('birth_of_baby', models.BooleanField(default=True)),
                ('baby_height', models.IntegerField(max_length=2)),
                ('baby_health', models.CharField(max_length=128)),
                ('birth_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('phone_num', models.IntegerField(max_length=24, serialize=False, primary_key=True)),
                ('mother_condition', models.CharField(max_length=128)),
                ('age', models.IntegerField(max_length=2)),
                ('geo_loc', models.IntegerField(max_length=6)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('give_aid', models.BooleanField(default=False)),
                ('receive_aid', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='baby',
            name='mother',
            field=models.ForeignKey(to='betterbirth.Mother'),
            preserve_default=True,
        ),
    ]
