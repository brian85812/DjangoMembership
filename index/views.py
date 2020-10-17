from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    users = User.objects.all()

    return render(request,"index.html",locals())