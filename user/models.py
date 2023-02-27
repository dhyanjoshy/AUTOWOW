from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dealer_id = models.AutoField(primary_key=True , unique=True)
    dealer=models.CharField(max_length=199)
    address_line1=models.CharField(max_length=199)
    address_line2=models.CharField(max_length=199, blank=True)
    address_line3=models.CharField(max_length=199, blank=True)
    location = models.URLField()
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField()

    def __str__(self) :
        return self.dealer

class Customer(models.Model):
    dealer = models.ForeignKey(Dealer , on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True , unique=True)
    fname=models.CharField(max_length=199)
    lname=models.CharField(max_length=199)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=False)


    def __str__(self) :
        name=self.fname+" "+self.lname
        return (name)