# -*- encoding: utf-8 -*-

from django.apps import AppConfig


class InitdataConfig(AppConfig):
    name = 'initdata'

    # # 初始化数据到内存中，重写ready函数
    def ready(self):
        from initdata.utils import data_initial
        print('init data .....')