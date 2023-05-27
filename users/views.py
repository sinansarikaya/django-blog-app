from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post

def dashboard(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'users/dashboard.html', {'posts':posts})

def profile(request):
    return render(request, 'users/profile.html')

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def logout_view(request):
    return redirect('/')


