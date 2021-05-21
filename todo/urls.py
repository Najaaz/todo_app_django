from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.log_in_view, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'todo/logout.html'), name='logout'),
]