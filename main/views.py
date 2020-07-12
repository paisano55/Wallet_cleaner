from django.shortcuts import render, redirect
from .models import Product
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def product_by_cate(request,cate):
    cate_dict={'computer':'컴퓨터','grocery':'식품/건강','digital':'디지털','homeapps':'가전/가구','cloth':'의류/잡화','extra':'기타'}
    prod_list = Product.objects.filter(category=cate_dict[cate])
    return render(request,"main.html",{'prod_list':prod_list})

def product_all(request):
    prod_list = Product.objects.all()
    return render(request,"main.html",{'prod_list':prod_list})

def regist(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])
            auth.login(request,user)
            return redirect('/products/')
        return render(request, 'register.html')
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

def favorite_list(request):
    fav_list = Product.objects.order_by('-date')
    return render(request,"favorite.html",{'fav_list':fav_list})

def fav_toggle(request,prod_pk):
    next_path = request.GET.get('next')
    # post_pk에 해당하는 Post객체
    post = get_object_or_404(Post, pk=prod_pk)
    # 요청한 사용자
    user = request.user

    # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
    filtered_like_posts = user.like_posts.filter(pk=post.pk)
    # 존재할경우, like_posts목록에서 해당 Post를 삭제
    if filtered_like_prods.exists():
        user.like_posts.remove(post)
    # 없을 경우, like_posts목록에 해당 Post를 추가
    else:
        user.like_prods.add(post)

    # 이동할 path가 존재할 경우 해당 위치로, 없을 경우 Post상세페이지로 이동
    if next_path:
        return redirect(next_path)
    return redirect('post:post_detail', post_pk=prod_pk)
