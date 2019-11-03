from django.shortcuts import render, redirect
from .forms import Login, Register
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('post:all_posts')
            else:
                return render(request, 'mylogin/login_error.html')
        else:
            form = Login()
        return render(request, 'mylogin/login.html', {'form':form})
    else: 
        return redirect('post:all_posts')


def logout_view(request):
    logout(request)
    return redirect('post:all_posts')


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], 
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'],
                                            first_name= form.cleaned_data['first_name'],
                                            last_name= form.cleaned_data['last_name'])
            user.save()
            return redirect('post:login')
        else:
            return render(request, 'mylogin/login_error.html')
    else:
        form = Register()
    return render(request, 'mylogin/register.html', {'form':form})