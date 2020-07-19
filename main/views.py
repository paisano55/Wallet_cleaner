from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Like, End
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
# Create your views here.

def product_by_cate(request,cate):
    cate_dict={'computer':'컴퓨터','grocery':'식품/건강','digital':'디지털','homeapps':'가전/가구','cloth':'의류/잡화','extra':'기타'}
    prod_list = Product.objects.filter(category=cate_dict[cate])
    return render(request,"main.html",{'prod_list':prod_list})

def product_all(request):
    prod_list = Product.objects.all()
    return render(request,"main.html",{'prod_list':prod_list})

def favorite_list(request):
    fav_list = request.user.like_prods.all()
    print(fav_list)
    return render(request,"main.html",{'prod_list':fav_list})

def regist(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
                auth.login(request,user)
                return redirect('/products/')
            except:
                return render(request, 'register.html',{'error': '이미 존재하는 ID입니다.'})
        else:
            return render(request, 'register.html',{'error': '비밀번호가 다릅니다.'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/products/')
        else:
            return render(request, 'login.html', {'error': '아이디나 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/products/')

@login_required
@require_POST
def prod_like(request):
    pk = request.POST.get('pk',None)
    prod = get_object_or_404(Product, pk=pk)
    prod_like, prod_like_created = prod.like_set.get_or_create(user=request.user)
    if not prod_like_created:
        prod_like.delete()
        message = "Favorite Cancel"
    else:
        message = "Favorite"
     
    context={'like_count':prod.like_count(),'message':message,'username':request.user.username,'add':prod_like_created}
    print(context)
    return HttpResponse(json.dumps(context))

@login_required
@require_POST
def end_vote(request):
    pk = request.POST.get('pk',None)
    prod = get_object_or_404(Product, pk=pk)
    prod_end, prod_end_created = prod.end_set.get_or_create(user=request.user)
    if not prod_end_created:
        message = "End vote cancel"
    else:
        message = "End vote added"
     
    context={'end_count':prod.end_count,'message':message,'username':request.user.username,'add':prod_end_created}
    return HttpResponse(json.dumps(context), content_type="application/json")

