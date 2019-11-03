from django.shortcuts import render, redirect
from .models import Post
from .forms import Add_post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
def post_view(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        return render(request, 'post/my_posts.html', {'posts': posts})
    else:
        return redirect('mylogin:login')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if (post.user == request.user) or (post.is_shared == True):
        return render(request, 'post/post.html', {'post': post})
    else:
        return render(request, 'post/restricted.html')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Add_post(request.POST)
            if form.is_valid:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('post:post_detail', post.id)
        else:
            form = Add_post()
        return render(request, 'post/add_post.html',{'form':form})
    else:
        return redirect('mylogin:login')


def all_posts(request):
    if request.user.is_authenticated:
        query = Post.objects.filter(user=request.user) | Post.objects.filter(is_shared=True)
    else:
        query = Post.objects.filter(is_shared=True)
    paginator = Paginator(query, 15)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'post/all_posts.html',{'posts':posts})


def user_posts(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user == request.user:
        return redirect('post:my_posts')
    else:
        posts = Post.objects.filter(user=user, is_shared=True)

    return render(request, 'post/user_posts.html', {'posts':posts})

             