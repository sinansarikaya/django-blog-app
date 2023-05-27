from django.shortcuts import render, redirect, get_object_or_404

def login_view(request):
    return render(request, 'blog/login.html')

def register_view(request):
    return render(request, 'blog/register.html')

def logout_view(request):
    return redirect('/')


