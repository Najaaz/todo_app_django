from django.core import serializers
from django.http import HttpResponse, request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api import serializers
from .models import Task
from api import permissions

# Create your views here.

class ListView(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    permission_classes = (IsAuthenticated, permissions.ViewOwnTask)
    # queryset = Task.objects.filter(user=request.user)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

