from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('products/',views.product_list),
]