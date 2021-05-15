from django.urls import path, include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('task', views.ListView, basename='task')


urlpatterns = [
    path('', include(router.urls)),
]