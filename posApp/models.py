from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.db.models.functions import Now

# Create your models here.

# class Employees(models.Model):
#     code = models.CharField(max_length=100,blank=True)
#     firstname = models.TextField()
#     middlename = models.TextField(blank=True,null= True)
#     lastname = models.TextField()
#     gender = models.TextField(blank=True,null= True)
#     dob = models.DateField(blank=True,null= True)
#     contact = models.TextField()
#     address = models.TextField()
#     email = models.TextField()
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
#     position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
#     date_hired = models.DateField()
#     salary = models.FloatField(default=0)
#     status = models.IntegerField()
#     date_added = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ExpiredManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
            expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
        )

class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    quantity = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_added = models.DateTimeField(blank=True, null=True,default=timezone.now)
    valid_to = models.DateTimeField(blank=False, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    objects = ExpiredManager()

    def __str__(self):
        return self.code + " - " + self.name


class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)
