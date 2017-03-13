# -*- codnig:utf-8 -*-

from .models import ProjectBaseInfo, ProjectItemValues
from rest_framework import serializers


class ProjectBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBaseInfo
        fields = ('id', 'pro_name', 'description', 'item_name')


class ProjectItemValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItemValues
        fields = ('id', 'pro_name', 'item_key', 'values')
