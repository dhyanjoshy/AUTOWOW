from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from store.models import Category
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from store.views import home

# Create your views here.
def login(request):
    form=Dealerform()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            has_profile = hasattr(user, 'dealer')
            if has_profile:
                auth_login(request, user)
                return redirect('/user/dashboard')
            else:
                return HttpResponse("Complete Profile")
                
            
        else :
            return HttpResponse("an error occured")
        
    
    cat=Category.objects.all()
    return render(request,"user/login_page.html",{'cat':cat,'forms':form})

def dashboard(request):
    return render(request,"user/dashboard.html")

def logout(request):
    auth_logout(request)
    return home(request)