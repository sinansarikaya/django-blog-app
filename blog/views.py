from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    return render(request, 'blog/index.html')

def post_detail(request, slug):
    pass

@login_required
def post_create(request):
    pass

@login_required
def post_edit(request, slug):
    pass


@login_required
def add_comment(request, slug):
    pass

@login_required
def comment_approve(request, pk):
    pass


