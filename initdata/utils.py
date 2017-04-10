# -*- encoding: utf-8 -*-

from common.decorators import singleton
from .models import ProjectBaseInfo, ProjectItemValues, DataArrayMemory

# 数据初始化
@singleton
class DataIniting():
    def __init__(self):
        # 用于存储各应用的基本信息，project_base_info
        self.project_base_info = {}
        # 存储各应用的各详细信息，project_item_values
        self.project_item_values = {}
        # 将数据存储在数组中
        self.comb_data_memory = []

        try:
            print('init data begin ...')
            pro_data = ProjectBaseInfo.objects.all().order_by('-id')
            # 遍历所用应用的数据存储到project_base_info字典中去
            for d in pro_data:
                pro_name = d.pro_name
                self.project_base_info[d.pro_name] = d.description + '#' + d.item_name
                # 取得某个应用里所有数据
                pro_items = ProjectItemValues.objects.filter(pro_name=pro_name)
                # 用于存储各应用里的数据
                item_values = {}
                for item in pro_items:
                    if item.item_key:
                        item_values.setdefault(item.item_key, item.values)
                    
                self.project_item_values[pro_name] = item_values
            print('====================')
            print('init data finish...')
        except Exception as e:
            pass

        try:
            print('init data to comb_data_memory')
            array_data = DataArrayMemory.objects.all().order_by('array_index')
            for d in array_data:
                self.comb_data_memory.append(d.values)
            print('============init data to comb_data_memory finished==============')
        except Exception as e:
            pass

    def get_data_dict(self):
        data_dict = self.dataDict
        return data_dict

data_initial = DataIniting()


