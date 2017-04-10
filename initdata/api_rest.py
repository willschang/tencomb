# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProjectBaseInfoSerializer, ProjectItemValuesSerializer, DataArrayMemorySerializer
from rest_framework.decorators import list_route, detail_route
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from .models import ProjectBaseInfo, ProjectItemValues, DataArrayMemory
from .utils import data_initial

# 存储平台上的各项目基础信息PROJECT_BASE_INFO
PROJECT_BASE_INFO = data_initial.project_base_info
# 存储平台上的各项目的各应用基础信息PROJECT_ITEM_VALUES
PROJECT_ITEM_VALUES = data_initial.project_item_values
# 存储平台上数据到COMB_DATA_MEMORY
COMB_DATA_MEMORY = data_initial.comb_data_memory
# 
LATEST_ARRAY_INDEX = len(COMB_DATA_MEMORY) if len(COMB_DATA_MEMORY) else 0



class ProjectBaseViewSet(viewsets.GenericViewSet):
    '''
    平台上各项目数据设置与读取
    '''
    queryset = ProjectBaseInfo.objects.all()
    serializer_class = ProjectBaseInfoSerializer

    @csrf_exempt
    @list_route(methods=['POST'])
    def set_project_info(self, request, *args, **kwargs):
        '''
        设置项目的基础信息

        '''
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            pro_name = data.get('pro_name')

            if pro_name in PROJECT_BASE_INFO.keys():
                return Response({'error': '该项目名已存在，请重新设置名称！'})
            else:
                # 事务处理
                with transaction.atomic():
                    # 保存数据到数据库
                    serializer.save()
                    # 将数据同步到内存变量中去
                    PROJECT_BASE_INFO[pro_name] = data.get('description', ' ') + '#' + data.get('item_name', ' ')
                    PROJECT_ITEM_VALUES[pro_name] = {}
                    return Response({'status': 'ok'})
                    # return Response({pro_name: PROJECT_BASE_INFO[pro_name]})
        else:
            error_info = serializer.errors

            return Response({'error': error_info})

    @list_route(methods=['GET'])
    def get_project_baseinfo(self, request, *args, **kwargs):
        '''
        取得各项目基础信息

        '''

        return Response(PROJECT_BASE_INFO)

    @list_route(methods=['GET'])
    def get_project(self, request, *args, **kwargs):
        '''
        取得某个项目基础信息

        pro_name -- 项目名字

        '''
        pro_name = request.GET.get('pro_name')
        # print(pro_name)
        if pro_name and pro_name in PROJECT_BASE_INFO.keys():
            return Response({pro_name: PROJECT_BASE_INFO[pro_name]})
        else:
            return Response({'error': '项目名有误，请确认！'})

 
class ProjectItemValuesViewSet(viewsets.GenericViewSet):
    '''
    平台中各项目里的各应用信息设置与读取
    '''
    queryset = ProjectItemValues.objects.all()
    serializer_class = ProjectItemValuesSerializer

    @list_route(methods=['POST'])
    def set_proitem_value(self, request, *args, **kwargs):
        '''
        设置项目中各应用的基础信息

        '''

        serializer = self.get_serializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            data = serializer.data
            pro_name = data.get('pro_name')
            item_key = data.get('item_key')
            values = data.get('values') if data.get('values') else 'none'

            if pro_name not in PROJECT_BASE_INFO.keys():
                return Response({'error': '该项目名不存在，请重新输入！'})
            else:
                # 事务处理
                with transaction.atomic():
                    # print(item_key)
                    # print(values)
                    try:
                        # 将数据同步到内存变量中去
                        if item_key in PROJECT_ITEM_VALUES[pro_name].keys():
                            PROJECT_ITEM_VALUES[pro_name][item_key] = values
                            # 更新数据库数据
                            ProjectItemValues.objects.filter(pro_name=pro_name, item_key=item_key).update(values=values)
                        else:
                            PROJECT_ITEM_VALUES[pro_name].setdefault(item_key, values)
                            # 保存数据到数据库
                            serializer.save()
                        # print(ITEMVALUES[pro_name])
                    except Exception as e:
                        return Response({'error': e})
                    
                    return Response({'status': 'ok'})
        else:
            error_info = serializer.errors
            return Response({'error': error_info})


    @list_route(methods=['GET'])
    def get_proitem_value(self, request, *args, **kwargs):
        '''
        取得项目中某个应用基础信息

        pro_name -- 项目名称
        item_key -- 应用名
        '''
        pro_name = request.GET.get('pro_name')
        item_key = request.GET.get('item_key')

        if pro_name not in PROJECT_BASE_INFO.keys():
            return Response({'error': '项目名称不存在，请重新输入！'})
        else:
            return Response({pro_name: PROJECT_ITEM_VALUES[pro_name].get(item_key)})

    @list_route(methods=['GET'])
    def get_project_items(self, request, *args, **kwargs):
        '''
        取得项目中某个应用基础信息

        pro_name -- 项目名称
        '''
        pro_name = request.GET.get('pro_name')

        if pro_name not in PROJECT_BASE_INFO.keys():
            return Response({'error': '项目名称不存在，请重新输入！'})
        else:
            return Response({pro_name: PROJECT_ITEM_VALUES[pro_name]})



class DataArrayViewSet(viewsets.GenericViewSet):
    '''
    数据内存
    '''
    queryset = DataArrayMemory.objects.all()
    serializer_class = DataArrayMemorySerializer


    @list_route(methods=['POST'])
    def set_data_memory(self, request, *args, **kwargs):
        '''
        设置数据到内存

        '''        
        values = request.data.get('values', None)
        
        if values:            
            with transaction.atomic():
                try:
                    global LATEST_ARRAY_INDEX
                    # 持久化数据
                    data_memory = DataArrayMemory(array_index=LATEST_ARRAY_INDEX, values=values)
                    data_memory.save()
                    # 将数据存储到内存中
                    COMB_DATA_MEMORY.append(values)

                    LATEST_ARRAY_INDEX += 1
                    return Response({'index': LATEST_ARRAY_INDEX-1})
                except Exception as e:
                    Response({'error': e})
        else:
            return Response({'error': '请输入数值'})  

    @list_route(methods=['GET'])
    def get_data_index(self, request, *args, **kwargs):
        '''
        索引值从内存中读取数据

        index_value -- 索引值

        '''
        index_value = request.GET.get('index_value', None)

        if index_value.isdigit():
            global LATEST_ARRAY_INDEX
            index_value = int(index_value)
            if index_value < LATEST_ARRAY_INDEX:
                return Response(COMB_DATA_MEMORY[index_value])
            else:
                return Response({'error': '输入的索引值不存在，请重新输入！'})

        else:
            return Response({'error': '索引值必须为数字，请重新输入！'})

    @list_route(methods=['POST'])
    def update_data_index(self, request, *args, **kwargs):
        '''
        通过索引值更新信息

        index_value -- 索引值

        '''
        index_value = request.GET.get('index_value', None)
        values = request.data.get('values', ' ')
        # 判断输入值是否为数字
        if index_value.isdigit():
            global LATEST_ARRAY_INDEX
            index_int = int(index_value)
            # 判断索引值是否超出数组的index值
            if index_int < LATEST_ARRAY_INDEX:
                # 事务处理
                with transaction.atomic():
                    DataArrayMemory.objects.filter(array_index=index_int).update(values=values)
                    # 更新值到数组里
                    COMB_DATA_MEMORY[index_int] = values if values else ' '
                return Response({index_value: COMB_DATA_MEMORY[index_int]})
            else:
                return Response({'error': '输入的索引值不存在，请重新输入！'})
        else:
            return Response({'error': '索引值必须为数字，请重新输入！'})






