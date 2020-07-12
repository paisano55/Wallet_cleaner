from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200,default=None)
    link = models.CharField(max_length=200)
    mall_link = models.CharField(max_length=200)
    end_vote = models.IntegerField(default=0)

class Account(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

