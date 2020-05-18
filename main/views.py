from django.shortcuts import render
from .models import Product,Category
# Create your views here.

def product_list(request):
    category_list = Category.objects.order_by('-timestamp')
    return render(request,"main.html",{'category_list':category_list})