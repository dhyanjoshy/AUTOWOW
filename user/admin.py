from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display=['user','dealer','address_line1','address_line2']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','phone_number']