# -*- coding:utf-8 -*-

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProjectBaseInfoSerializer, ProjectItemValuesSerializer
from rest_framework.decorators import list_route, detail_route
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from .models import ProjectBaseInfo, ProjectItemValues
from .utils import data_initial

# 存储平台上的各项目基础信息PROJECT_BASE_INFO
PROJECT_BASE_INFO = data_initial.project_base_info
# 存储平台上的各项目的各应用基础信息PROJECT_ITEM_VALUES
PROJECT_ITEM_VALUES = data_initial.project_item_values


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





