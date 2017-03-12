# -*- encoding: utf8 -*-

from django.db import models


# 用于存储平台上各项目的基础数据 ProBaseTable
class ProjectBaseInfo(models.Model):
    pro_name = models.CharField('项目名称', max_length=50, db_index=True, unique=True, help_text='项目名称') 
    description = models.CharField('项目描述', max_length=200, default=None, null=True, help_text='项目描述')
    item_name = models.CharField('项目映射值', max_length=500, default=None, null=True, help_text=r'项目属性,如"ip,addr,port,..."')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

# 各项目的详细信息
class ProjectItemValues(models.Model): 
    pro_name = models.CharField('项目名称', max_length=50, db_index=True, help_text='项目名称')
    item_key = models.CharField('记录的key值', max_length=50, help_text='应用key值')
    values = models.CharField('记录值', db_index=True, max_length=1000, default='', help_text=r'应用的基本信息, 如"192.168.1.10,xiamen china,80,..."')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

# from initdata.utils import data_initial
# print('init data .....')