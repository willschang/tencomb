# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from initdata import api_rest

router = routers.DefaultRouter()
router.register(r'initdata/projects', api_rest.ProjectBaseViewSet)
router.register(r'initdata/items', api_rest.ProjectItemValuesViewSet)
router.register(r'initdata/data_array', api_rest.DataArrayViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]