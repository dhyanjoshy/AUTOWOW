from django.db import models
from user.models import Dealer

#category model for bike and cars
class Category(models.Model):
    
    title = models.CharField(max_length = 128, unique = True)
    image = models.ImageField(upload_to = 'images/category/')

    class Meta:
        verbose_name_plural='categories'

    def __str__(self) :
        return self.title

#category model brands (tata,maruthi)
class Brand(models.Model):

    brand_id = models.AutoField(primary_key=True,unique=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 128, unique = False)
    logo = models.ImageField(upload_to = 'image/Brand_logo/')
    description = models.TextField(blank = True)

    def __str__(self) :
        return self.title

class Product(models.Model):

    product_id = models.AutoField(primary_key=True,unique=True)
    dealer = models.ForeignKey(Dealer ,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'image/Product_image/')
    description = models.TextField(blank = True)

    def __str__(self) :
        return self.title

class Varient(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    title = models.CharField(max_length = 128, unique = False)
    price = models.IntegerField()

    def __str__(self) :
        return self.title

class Color(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    title = models.CharField(max_length = 128, unique = False)
    image = models.ImageField(upload_to = 'image/color/')
