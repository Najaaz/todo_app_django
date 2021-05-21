from django.core.serializers import serialize
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'task', 'date_created', 'completed')
        extra_kwargs = {
            "date_created":{"read_only":True},
            'completed':{"read_only":True}
        }


class TaskEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            "user":{"read_only":True},
            "task":{"read_only":True}
        }

