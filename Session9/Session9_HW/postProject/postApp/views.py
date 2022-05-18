from django.shortcuts import render, redirect
from postApp.models import Post, Comment

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request,'postApp/list.html', {'posts':posts})


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'] 
                
        )
        return redirect('detail', new_post.pk)
    return render(request,'postApp/new.html')


def detail(request,post_pk):
    post = Post.objects.get(pk=post_pk)  

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('detail', post_pk)
    return render(request, 'postApp/detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.filter(pk=post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    return render(request, 'postApp/edit.html',{'post':post[0]})


def delete(request,post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('list')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

