# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectBaseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pro_name', models.CharField(verbose_name='项目名称', max_length=50, unique=True, db_index=True)),
                ('description', models.CharField(verbose_name='项目描述', max_length=200, default=None, null=True)),
                ('item_name', models.CharField(verbose_name='项目映射值', max_length=500, default=None, null=True)),
                ('max_key', models.CharField(verbose_name='当前最大key值', max_length=50, default='0')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItemValues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pro_name', models.CharField(verbose_name='项目名称', max_length=50, db_index=True)),
                ('item_key', models.CharField(verbose_name='记录的key值', max_length=50)),
                ('values', models.CharField(verbose_name='记录值', max_length=1000, default=' ', db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
