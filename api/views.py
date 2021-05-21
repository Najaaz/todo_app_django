from django.core import serializers
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Task
from .permissions import ViewOwnTask
from .serializers import TaskSerializer, TaskEditSerializer

# Create your views here.


class ListCreateTaskAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class RetrieveUpdateDestroyTaskAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskEditSerializer
    # queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ViewOwnTask]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    # Create user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES