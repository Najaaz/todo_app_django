from django.urls import path, include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from api import views

# router = DefaultRouter()
# router.register('task', views.ListView, basename='task')


# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', views.ListCreateTaskAPIView.as_view(), name='task'),
    path('<int:pk>/', views.RetrieveUpdateDestroyTaskAPIView.as_view(), name='get_delete_update_task'),
    path('login/', views.UserLoginApiView.as_view()),
]