from django.shortcuts import render
from rest_framework import viewsets
from minister.coreauth import UserProfile
from asset.serializers import UserSerializer,AssetSerializer
from models import Asset
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer