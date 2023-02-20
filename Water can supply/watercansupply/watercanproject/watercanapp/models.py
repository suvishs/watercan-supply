from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=150)
    quantity = models.IntegerField()
    odr = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

class Usr_can_odr(models.Model):
    name = models.CharField(max_length=15)
    phone_no = models.CharField(max_length=13)
    adress = models.CharField(max_length=150)
    quantity = models.IntegerField()
    reason = models.CharField(max_length=150)
    usr_can = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

class com_can_odr(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=150)
    quantity = models.IntegerField()
    reason = models.CharField(max_length=150, null=True)
    com_can = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

class Delivered_his(models.Model):
    name = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=150)
    quantity = models.IntegerField()
    delv = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=15)
    contact_number = models.CharField(max_length=13)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name