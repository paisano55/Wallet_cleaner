from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200,default=None)
    link = models.CharField(max_length=200)
    mall_link = models.CharField(max_length=200)
    end_vote = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='end_user_set',through='End')
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='like_user_set',through='Like')

    @property
    def end_count(self):
        return self.end_vote.count()
    
    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    prod = models.ForeignKey(Product)


