from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','image']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=['title','logo','description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','title','image','description']

@admin.register(Varient)
class VarientAdmin(admin.ModelAdmin):
    list_display=['title','price']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=['title','image']