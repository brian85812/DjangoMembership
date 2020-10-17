from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        User.objects.create_user(username=name, password=password)

        return HttpResponseRedirect('/login/')

def login(request):
    if request.method == 'GET':
         return render(request, 'login.html')

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)

        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect('/login/')