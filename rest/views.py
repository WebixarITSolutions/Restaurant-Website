from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from database.models import Contactd
from database.models import Feedbackd
from database.models import Reserved

def home(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        data=request.POST.get('data')
        con=Contactd(name=name,email=email,data=data)
        con.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def reserve(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname1=request.POST.get('uname1')
        email2=request.POST.get('email2')
        num1=request.POST.get('num1')
        Time=request.POST.get('Time')
        en=Reserved(fname=fname,lname=lname,uname1=uname1,email2=email2,num1=num1,Time=Time)
        en.save()
    return render(request,'resgis.html')

def feed(request):
    if request.method=='POST':
        name1=request.POST.get('name1')
        email1=request.POST.get('email1')
        num=request.POST.get('num')
        feed=request.POST.get('feed')
        fe=Feedbackd(name1=name1,email1=email1,num=num,feed=feed)
        fe.save()
    return render(request,'Feedback.html')