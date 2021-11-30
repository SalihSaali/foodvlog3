from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name = request.POST['FIRST_NAME']
        last_name = request.POST['LAST_NAME']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Sorry,this username is already taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Sorry,this email is already taken')
                return redirect('Register')
            else:
                user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password1,)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print('Password is not match,try again')
            return redirect('Register')

    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password1']
        User = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,'Invalid details,try again')
            return redirect('Login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')