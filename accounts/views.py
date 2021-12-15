from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name = request.POST['FIRST_NAME']
        last_name = request.POST['LAST_NAME']
        username = request.POST['USERNAME']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Sorry,this username is already taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Sorry,this email is already taken')
                return redirect('Register')
            else:
                user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request,'Password is not match,try again')
            return redirect('Register')

    else:
        return render(request,'register.html')

def login_view(request):
    if request.method=="POST":
        username = request.POST['USERNAME']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid details,try again')
            return redirect('Login')
    else:
        return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')