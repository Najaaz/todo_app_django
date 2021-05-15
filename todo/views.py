import os
from django.http import response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required
def home(request):
    os.environ['NO_PROXY'] = '127.0.0.1'
    response = requests.get("http://127.0.0.1:8000/")
    print(response)
    context = {

    }
    return render(request, 'todo/home.html', context)


