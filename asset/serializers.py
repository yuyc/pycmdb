from minister.coreauth import UserProfile
from rest_framework import serializers
from models import Asset

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'mobile')

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ('name', 'sn')


