from django.shortcuts import render,HttpResponse,redirect
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
            user.is_active = False
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
            has_profile = hasattr(user, 'dealer')
            if has_profile:
                auth_login(request, user)
                return redirect('/user/dashboard')
            else:
                return HttpResponse("Complete profile")
        else:
            messages.error(request, 'Invalid form submission!!!')
    cat=Category.objects.all()
    return render(request,"user/login_page.html",{'cat':cat})


    



def dashboard(request):
    return render(request,"user/dashboard.html")

def logout(request):
    auth_logout(request)
    return home(request)