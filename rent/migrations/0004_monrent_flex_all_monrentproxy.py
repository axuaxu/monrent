# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_rentdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monrent_flex_all',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('num', models.CharField(blank=True, max_length=200, null=True)),
                ('udate', models.CharField(blank=True, max_length=200, null=True)),
                ('surl', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('pcode', models.CharField(blank=True, max_length=200, null=True)),
                ('rent', models.CharField(blank=True, max_length=200, null=True)),
                ('rstyle', models.CharField(blank=True, max_length=200, null=True)),
                ('method', models.CharField(blank=True, max_length=200, null=True)),
                ('rooms', models.CharField(blank=True, max_length=200, null=True)),
                ('length', models.CharField(blank=True, max_length=200, null=True)),
                ('intime', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, max_length=200, null=True)),
                ('tenant', models.CharField(blank=True, max_length=200, null=True)),
                ('treq', models.CharField(blank=True, max_length=200, null=True)),
                ('condition', models.CharField(blank=True, max_length=200, null=True)),
                ('equip', models.CharField(blank=True, max_length=200, null=True)),
                ('env', models.CharField(blank=True, max_length=200, null=True)),
                ('bus', models.CharField(blank=True, max_length=200, null=True)),
                ('metro', models.CharField(blank=True, max_length=200, null=True)),
                ('train', models.CharField(blank=True, max_length=200, null=True)),
                ('hway', models.CharField(blank=True, max_length=200, null=True)),
                ('oname', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('phone2', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('wechat', models.CharField(blank=True, max_length=200, null=True)),
                ('qq', models.CharField(blank=True, max_length=200, null=True)),
                ('aprice', models.CharField(blank=True, max_length=200, null=True)),
                ('atitle', models.CharField(blank=True, max_length=200, null=True)),
                ('abus', models.CharField(blank=True, max_length=200, null=True)),
                ('ametro', models.CharField(blank=True, max_length=200, null=True)),
                ('atrain', models.CharField(blank=True, max_length=200, null=True)),
                ('ahway', models.CharField(blank=True, max_length=200, null=True)),
                ('area1', models.CharField(blank=True, max_length=200, null=True)),
                ('area2', models.CharField(blank=True, max_length=200, null=True)),
                ('area3', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonrentProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('rent.monrent',),
        ),
    ]
