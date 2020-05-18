from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(default=0)
    shipping_fee = models.IntegerField(default=0)
    mall = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    end_vote = models.IntegerField(default=0)


