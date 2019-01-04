from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_bridge.news.serializers import UserSerializer, GroupSerializer, NewsSerializer
from django_bridge.news.models import News

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer