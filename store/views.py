from django.shortcuts import render,HttpResponse
from .models import *
from .forms import UserForm
from django.contrib import messages


def home(request):
    category=Category.objects.all()
    return render(request,"home.html",{"cat":category})

def brand(request,brand):
    category=Category.objects.all()
    brand=Brand.objects.filter(category__title=brand)
    return render(request,"store/brand.html",{'brand':brand,"cat":category})

def products(request,brand_id):
    category=Category.objects.all()
    product=Product.objects.filter(brand__brand_id=brand_id)
    return render(request,"store/product.html",{'product':product,"cat":category})

def single_product(request,product_id):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                return HttpResponse(request, 'Some error!')
            messages.success(request, 'Your form has been submitted successfully.')
            category=Category.objects.all()
            product=Product.objects.get(product_id=product_id)
            color=Color.objects.filter(product__product_id=product_id)
            varient=Varient.objects.filter(product__product_id=product_id)
            return render(request,"store/single_product.html",{"product":product,"cat":category,"color":color,"varient":varient,'messages':messages,'form':form})
    else:
        form = UserForm()
    category=Category.objects.all()
    product=Product.objects.get(product_id=product_id)
    color=Color.objects.filter(product__product_id=product_id)
    varient=Varient.objects.filter(product__product_id=product_id)
    return render(request,"store/single_product.html",{"product":product,"cat":category,"color":color,"varient":varient,'form':form})

def loan_calculator(request):
    category=Category.objects.all()
    return render(request,"store/loan_calculator.html",{"cat":category})