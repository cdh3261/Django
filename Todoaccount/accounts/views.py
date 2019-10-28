from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/form.html',context)

def login(request):

    if request.user.is_authenticated:
        return redirect('todos:index')

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 여기까지가 로그인 로직

            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/form.html',context)

def logout(request):
    auth_logout(request)
    return redirect('todos:index')