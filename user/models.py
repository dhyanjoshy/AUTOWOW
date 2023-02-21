from django.db import models

# Create your models here.

class Dealer(models.Model):
    dealer_id = models.AutoField(primary_key=True , unique=True)
    username=models.CharField(max_length=199)
    password=models.CharField(max_length=199)
    dealer=models.CharField(max_length=199)
    address_line1=models.CharField(max_length=199)
    address_line2=models.CharField(max_length=199, blank=True)
    address_line3=models.CharField(max_length=199, blank=True)
    location = models.URLField()
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self) :
        return self.dealer

class User(models.Model):
    dealer = models.ForeignKey(Dealer , on_delete=models.CASCADE)
    user_id = models.AutoField(primary_key=True , unique=True)
    fname=models.CharField(max_length=199)
    lname=models.CharField(max_length=199)
    email = models.EmailField(unique=True)
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField()

    def __str__(self) :
        return (self.fname,self.lname)