# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yz', '0006_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='YzPeople',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'yz_people',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='people',
        ),
    ]
