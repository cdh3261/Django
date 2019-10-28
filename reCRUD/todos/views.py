from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

# 사용자의 폼을 보여주는 new파일
def new(request):
    return render(request, 'new.html')

# 사용자가 입력한 폼을 저장하는 create파일
def create(request):
    title = request.GET.get('title')
    due_date = request.GET.get('duedate')

    todo = Todo()
    todo.title = title
    todo.due_date = due_date
    todo.save() # 데이트베이스에 저장함. 이순간 데이터베이스 시작!

    return redirect('/todos/')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/')

def edit(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo' : todo
    }
    return render(request, 'edit.html', context)

def update(request, id):
    todo = Todo.objects.get(id=id)
    title = request.GET.get('title')
    due_date = request.GET.get('duedate')

    todo.title = title
    todo.due_date = due_date

    todo.save()
    return redirect('/todos/')