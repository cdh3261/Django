from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # django에서만 저장하고 데이터베이스에는 아직 저장하지 않는다.
            post.user = request.user
            post.save()
            return redirect('posts:index')

    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/form.html', context)

def like(request,id):
    post = get_object_or_404(Post,id=id)
    user = request.user

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('posts:index')