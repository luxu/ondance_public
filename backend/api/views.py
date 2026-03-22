# from rest_framework import viewsets
# from rest_framework import permissions
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics
# from django.core.paginator import Paginator

from api.serializers import UserSerializer

from user.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

users = UserList.as_view()


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

create_user = UserCreate.as_view()
