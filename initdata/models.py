# -*- encoding: utf8 -*-

from django.db import models


# 用于存储平台上各项目的基础数据 ProBaseTable
class ProjectBaseInfo(models.Model):
    pro_name = models.CharField('项目名称', max_length=250, db_index=True, unique=True, help_text='项目名称') 
    description = models.CharField('项目描述', max_length=200, help_text='项目描述')
    item_name = models.TextField('项目映射值', help_text='项目属性,如"ip,addr,port,..."')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# 各项目的详细信息
class ProjectItemValues(models.Model): 
    pro_name = models.CharField('项目名称', max_length=250, db_index=True, help_text='项目名称')
    item_key = models.CharField('记录的key值', max_length=100, help_text='应用key值')
    values = models.TextField('记录值', help_text='应用的基本信息, 如"192.168.1.10,xiamen china,80,..."')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    