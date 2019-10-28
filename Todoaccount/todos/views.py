from django.shortcuts import render,redirect,get_object_or_404
from IPython import embed
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from .models import Todo


# Create your views here.
@login_required
def index(request):
    # visit_num = request.session.get('visit_num',0)
    # request.session['visit_num'] = visit_num+1

    # request.session.modified = True

    # context = {
    #     'visit_num': visit_num
    # }

    todos = request.user.todo_set.all().order_by('due_date')
    context = {
        'todos':todos,
    }

    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == "POST":
        pass
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request,'todos/form.html',context)

def delete(request,id):
    todo = get_object_or_404(Todo, id=id)
    if todo.user == request.user:
        todo.delete()
        return redirect('todos:index')