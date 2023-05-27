from django.shortcuts import render, redirect, get_object_or_404

def dashboard(request):
    posts = [
        {
            "id": 1,
            "title": "Örnek Blog Başlığı 1",
            "date": "2023-05-10"
        },
        {
            "id": 2,
            "title": "Örnek Blog Başlığı 2",
            "date": "2023-05-15"
        },
        {
            "id": 3,
            "title": "Örnek Blog Başlığı 3",
            "date": "2023-05-20"
        }
    ]
    return render(request, 'users/dashboard.html', {'posts':posts})

def profile(request):
    return render(request, 'users/profile.html')

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/register.html')

def logout_view(request):
    return redirect('/')


