from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
#from . models import Blog


def index(request):
    return render(request, "auth_app/index.html")

def login_page(request):
    if request == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

def logout_page(request):
    if request == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")


def register(request):
    if request == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

