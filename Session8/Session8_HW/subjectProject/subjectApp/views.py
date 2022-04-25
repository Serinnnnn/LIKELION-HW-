from django.shortcuts import render, redirect

from subjectApp.forms import SubjectModelForm
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

    # views.py가 무조건 함수일 필요는 없고 class형 view라고 하는 것임. 
    # CreateView 라는게 장고에서 이미 만들어진 것.
    # 상속을 이용해서 장고에서 준비해둔 것을 사용해서 최소한의 것만 넣어주면 동작하게끔 편의를 위한 것임.나중에 많이 쓰진 않음. 이런게 있다 정도만

def home(request):
    subjects = Subject.objects.all()
    majors = Major.objects.all()

    return render(request, 'home.html', {'subjects':subjects, 'majors': majors})


class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def computerSubjectView(request):
    subjects = Subject.objects.all()
    computerMajor = subjects.filter(major__title='컴퓨터학과')
    return render(request, 'computer.html', {'computerMajor': computerMajor})


class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')

def DeleteSubjectView(request, subject_pk):
    delSubject = Subject.objects.get(pk=subject_pk)
    delSubject.delete()
    return redirect('home')


class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'editMajor.html'
    success_url = reverse_lazy('home')

def DeleteMajorView(request, major_pk):
    delMajor = Major.objects.get(pk=major_pk)
    delMajor.delete()
    return redirect('home')