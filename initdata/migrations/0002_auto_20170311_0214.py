# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('initdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectbaseinfo',
            name='max_key',
        ),
        migrations.AlterField(
            model_name='projectbaseinfo',
            name='description',
            field=models.CharField(max_length=200, help_text='项目描述', null=True, verbose_name='项目描述', default=None),
        ),
        migrations.AlterField(
            model_name='projectbaseinfo',
            name='item_name',
            field=models.CharField(max_length=500, help_text='项目属性,如"ip,addr,port,..."', null=True, verbose_name='项目映射值', default=None),
        ),
        migrations.AlterField(
            model_name='projectbaseinfo',
            name='pro_name',
            field=models.CharField(max_length=50, unique=True, help_text='项目名称', db_index=True, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='projectitemvalues',
            name='item_key',
            field=models.CharField(max_length=50, help_text='应用key值', verbose_name='记录的key值'),
        ),
        migrations.AlterField(
            model_name='projectitemvalues',
            name='pro_name',
            field=models.CharField(max_length=50, db_index=True, help_text='项目名称', verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='projectitemvalues',
            name='values',
            field=models.CharField(max_length=1000, db_index=True, help_text='应用的基本信息, 如"192.168.1.10,xiamen china,80,..."', verbose_name='记录值', default=''),
        ),
    ]
