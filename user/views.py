from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from store.models import Category
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.contrib import messages
from store.views import home


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('/user/login')
    else:
        form = SignUpForm()
    cat=Category.objects.all()
    return render(request,"user/signup_page.html",{'cat':cat,'form':form})

def login(request):
    if request.method == 'POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("test")    
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)            
            has_profile = hasattr(user, 'dealer')
            if has_profile:
                return redirect('/user/dashboard')
            else:
                return redirect('/user/dealerdetails')
        else:
            messages.error(request, 'Username or password is incorrect !')
    cat=Category.objects.all()
    return render(request,"user/login_page.html",{'cat':cat})


    

def dealerdetails(request):
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            return redirect('/user/login')
    else:
        form = DealerForm()

    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dealerform.html",{'cat':cat,'username':user,'form':form})


def dashboard(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dashboard.html",{'cat':cat,'user':user})

def dash_home(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dashboard.html",{'cat':cat,'user':user})

def logout(request):
    auth_logout(request)
    return home(request)