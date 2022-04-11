from django.shortcuts import render,redirect
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts': posts})


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title= request.POST['title'],
            content= request.POST['content']
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

    # request의 POST에 있는 title 로 가게됨. request는 브라우저가 우리한테 주는 요청 객체
    # new_post.pk가 경로변수, 방금 전 생성한 post의 pk값
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html',{'post':post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        updated_post= Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail',post_pk)
    return render(request, 'edit.html',{'post':post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')


    

