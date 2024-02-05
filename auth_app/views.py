from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from . models import Blog

@login_required(login_url="/auth_app/login")
def index(request):
    return render(request, "auth_app/index.html")

def login_page(request):
    if request.method == 'POST':    
        username = request.POST['username']
        pass1 = request.POST['pass1']
        print(username)
        print(pass1)

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect("loginpage")
        user = authenticate(username = username, password = pass1)
        fname = user.first_name

        if user is not None:
             login(request, user)
             #return render(request, "auth_app/index.html", {'fname': fname})
             return redirect("index")
        else:
            messages.error(request, "Bad credentials")
            return redirect("loginpage")
        
    return render(request, "auth_app/login.html")
        

def logout_page(request):
    logout(request)
    return redirect("loginpage")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        

        user = User.objects.create_user(username)
        user.first_name = fname
        user.last_name = lname
        user.set_password(pass1)

        user.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("loginpage")

    return render(request, "auth_app/register.html")