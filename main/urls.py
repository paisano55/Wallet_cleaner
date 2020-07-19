from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('',views.product_all),
    path('products/',views.product_all),
    path('products/<str:cate>/',views.product_by_cate),
    path('login/',views.login),
    path('register/',views.regist),
    path('logout/',views.logout),
    path('favorites/',views.favorite_list),
    path('like/',views.prod_like,name="prod_like"),
    path('endvote/',views.end_vote,name="end_vote"),
]