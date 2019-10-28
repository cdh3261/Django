from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }

    return render(request, 'index.html', context)

def create(request):
    # post이면 db저장
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due-date')
        todo.save()
        return redirect('todos:index')
    else:
        return render(request, 'create.html')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos:index')

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method=='POST':
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due-date')
        todo.save()
        return redirect('todos:index')
    else:
        context = {
            'todo' : todo
        }
        return render(request, 'update.html', context)