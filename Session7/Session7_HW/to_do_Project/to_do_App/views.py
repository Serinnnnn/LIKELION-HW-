from django.shortcuts import render, redirect

import to_do_Project
from .models import To_do
# Create your views here.

def home(request):
    To_dos = To_do.objects.all()

    return render(request, 'home.html', { 'To_dos' : To_dos })


def new(request):
    if request.method == 'POST' :
        new_To_do = To_do.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', new_To_do.pk)
    return render(request, 'new.html')

def detail(request, Todo_pk):
    Todo = To_do.objects.get(pk=Todo_pk)
    Todo_deadline = Todo.deadline.strftime('%Y-%m-%d')
    return render(request, 'detail.html', {
        'Todo': Todo,
        'Todo_deadline': Todo_deadline})
    

def edit(request, Todo_pk):
    Todo = To_do.objects.get(pk=Todo_pk)
    Todo_deadline = Todo.deadline.strftime('%Y-%m-%d')
    if request.method == 'POST':
        updated_Todo = To_do.objects.filter(pk=Todo_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('home')
    
    return render(request, 'edit.html', {
        'Todo':Todo,
        'Todo_deadline': Todo_deadline })

def delete(request, Todo_pk):
    Todo = To_do.objects.get(pk=Todo_pk)
    Todo.delete()

    return redirect('home')




            
        