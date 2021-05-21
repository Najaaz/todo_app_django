import os, json
from dateutil import parser
from django.http import response
from django.utils import timezone
from django.urls.conf import path
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import requests
from requests.sessions import session
from rest_framework import authentication

# Create your views here.

@login_required
def home(request):
    r = requests.get("http://127.0.0.1:8000/api/", headers={"Authorization":request.session["token"]})
    tasks = json.loads(r.text)

    timing = []
    for item in tasks:
        time = parser.parse(item.get('date_created'))
        timing.append(time)


    context = {
        "tasks":zip(timing, tasks),
        "current_time":timezone.now()
    }
    return render(request, 'todo/home.html', context)



def log_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            response = requests.post("http://127.0.0.1:8000/api/login/", data={"username":username, "password":password})
            token =  json.loads(response.text).get("token")
            request.session["token"] = f"Token {token}"
            request.session.modified = True
            
            return redirect("home")
        else:
            return render(request, "todo/login.html", {"message":"Your entered credentials are wrong"})

    else:
        return render(request, "todo/login.html")