# -*- encoding: utf-8 -*-

from common.decorators import singleton
from .models import ProjectBaseInfo, ProjectItemValues

# 数据初始化
@singleton
class DataIniting():
    def __init__(self):
        # 用于存储各应用的基本信息，proBase
        self.proBase = {}
        # 存储各应用的各详细信息，proItemValue
        self.proItemValue = {}

        pro_data = ProjectBaseInfo.objects.all().order_by('-id')
        # 遍历所用应用的数据存储到proBase字典中去
        for d in pro_data:
            pro_name = d.pro_name
            self.proBase[d.pro_name] = d.description + '#' + d.item_name
            # 取得某个应用里所有数据
            pro_items = ProjectItemValues.objects.filter(pro_name=pro_name)
            # 用于存储各应用里的数据
            item_values = {}
            for item in pro_items:
                if item.item_key:
                    item_values.setdefault(item.item_key, item.values)
                
            self.proItemValue[pro_name] = item_values
        print(self.proBase)
        print('====================')
        print(self.proItemValue)
       

    def get_data_dict(self):
        data_dict = self.dataDict
        return data_dict

data_initial = DataIniting()


