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
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)            
            has_profile = hasattr(user, 'dealer')
            if has_profile:
                return redirect('/user/dash_home')
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
            return redirect('user:dash_home')
    else:
        form = DealerForm()

    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dealerform.html",{'cat':cat,'username':user,'form':form})


def dashboard(request):
    if request.user.is_authenticated:
        # User is logged in, redirect to dash_home
        return redirect('user:dash_home')
    else:
        # User is not logged in, redirect to login
        return redirect('user:login')

def dash_home(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dash_home.html",{'cat':cat,'user':user})


def dash_addbrand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            return redirect('user:dash_home')
    else:
        form = BrandForm()
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dash_addbrand.html",{'cat':cat,'user':user,'form':form})

def dash_addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            return redirect('user:dash_home')
    else:
        form = ProductForm()
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    return render(request,"user/dash_addproduct.html",{'cat':cat,'user':user,'form':form})

def dash_urproduct(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    dealer_id=user.dealer.dealer_id
    product=Product.objects.filter(dealer__dealer_id=dealer_id)
    return render(request,"user/dash_urproduct.html",{'cat':cat,'user':user,'product':product})

def dash_single_product(request,product_id):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    product=Product.objects.get(product_id=product_id)
    color=Color.objects.filter(product__product_id=product_id)
    varient=Varient.objects.filter(product__product_id=product_id)
    return render(request,"user/dash_single_product.html",{'cat':cat,'user':user,'product':product,'color':color,'varient':varient})

def dash_addcolor(request,product_id):
    if request.method == 'POST':
        form = ColorForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            return redirect('user:dash_home')
    else:
        form = ColorForm()
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    product=Product.objects.get(product_id=product_id)
    return render(request,"user/dash_addcolor.html",{'cat':cat,'user':user,'form':form,'product':product})

def dash_addvarient(request,product_id):
    if request.method == 'POST':
        form = VarientForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            return redirect('user:dash_home')
    else:
        form = VarientForm()
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    product=Product.objects.get(product_id=product_id)
    return render(request,"user/dash_addvarient.html",{'cat':cat,'user':user,'form':form,'product':product})


def dash_enquiries(request):
    username=request.user.username
    user = get_object_or_404(User, username=username)
    cat=Category.objects.all()
    dealer_id=user.dealer.dealer_id
    customer=Customer.objects.filter(dealer__dealer_id=dealer_id)
    return render(request,"user/dash_enquiries.html",{'cat':cat,'user':user,'customer':customer})


def logout(request):
    auth_logout(request)
    return home(request)