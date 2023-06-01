from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.conf import settings
from google.cloud import storage

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False, status='published').order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post, is_approved=True)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        form.instance.slug = slugify(form.instance.title)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post başarıyla oluşturuldu.')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, f'Form hatalı: {form.errors}')
                           
    else:     
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form':form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        raise PermissionDenied()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail', {'form': form, 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        raise PermissionDenied()

    try:
        # Google Cloud Storage'daki resmi sil
        if post.featured_image:
            client = storage.Client(credentials=settings.GS_CREDENTIALS)
            bucket = client.get_bucket(settings.GS_BUCKET_NAME)
            blob = bucket.blob(post.featured_image.name)
            blob.delete()

        # Post'u veritabanından sil
        post.delete()
    except Exception as e:
        print(f'Hata: {e}')  # Hata mesajını yazdır
        messages.error(request, f'Gönderi silinirken bir hata oluştu: {e}')
        return redirect('dashboard')

    return redirect('dashboard')

