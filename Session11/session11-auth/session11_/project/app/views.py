from turtle import title
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth 
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()

    return render(request, "home.html", {"posts": posts})


@login_required(login_url="/registration/login")
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect("detail", new_post.pk)

    return render(request, "new.html")


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.filter(pk=post_pk).update(title=title, content=content)
        return redirect("detail", post_pk)

    return render(request, "edit.html", {"post": post})

@login_required(login_url="/registration/login")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        content = request.POST["content"]
        Comment.objects.create(post=post, content=content, author=request.user)

        return redirect("detail", post_pk)
    return render(request, "detail.html", {"post": post})


def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("detail", post_pk)


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect("home")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect("home")
    return render(request, "registration/signup.html")
        # create_user: user객체 생성하고 저장해줌 

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get("next", "/"))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})
    
    return render(request, "registration/login.html")

# 장고에서 request 내용을 뽑아내고 싶을 때,
# request.GET : request 데이터를 딕셔너리 형태로 변환 dict.get(key) : 딕셔너리 관련 함수로써 key값을 통해 value를 얻어냄


def logout(request):
    auth.logout(request)

    return redirect("home")

