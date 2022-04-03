from django.shortcuts import render, redirect
from .models import Article
import time


# Create your views here.
def new(request):
    if request.method == 'POST':
        print(request.POST)
        article_time = time.strftime('%Y-%m-%d', time.localtime(time.time())) + time.strftime('%c', time.localtime(time.time()))
        new_article= Article.objects.create(
            title = request.POST['title'],
            content= request.POST['content'],
            category = request.POST['category'],
            time=article_time

        )
        return redirect('index')

    return render(request, 'new.html')


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html',{'article': article})

def index(request):
    Hobby_number = Article.objects.filter(category="Hobby").count()
    Food_number = Article.objects.filter(category="Food").count()
    Programming_number = Article.objects.filter(category="Programming").count()
    return render(request, 'index.html', {'Hobby': Hobby_number, 'Food': Food_number, 'Programming': Programming_number})

def Hobby(request):
    Hobby = Article.objects.filter(category="Hobby")
    return render(request, 'Hobby.html', {'articles' : Hobby})

def Food(request):
    Food = Article.objects.filter(category="Food")
    return render(request, 'Food.html', {'articles' : Food})

def Programming(request):
    Programming = Article.objects.filter(category="Programming")
    return render(request, 'Programming.html', {'articles' : Programming})

    
