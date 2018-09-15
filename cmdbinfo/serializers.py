#_*_coding:utf-8_*_

from cmdbinfo.myauth import UserProfile
from cmdbinfo import models
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'name', 'email')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        depth=2
        fields = ('url','name', 'sn','server','networkdevice','asset_type')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        fields = ('url','sub_asset_type',)

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RAM
        fields = ('url','sn','model','slot','capacity',)

