from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from blog.models import Post

def dashboard(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'users/dashboard.html', {'posts':posts})

def profile(request):
    return render(request, 'users/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    return render(request, 'users/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')


