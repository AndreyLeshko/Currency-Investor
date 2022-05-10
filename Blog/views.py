from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from . import forms

def show_all_post(request):
    posts = Post.objects.all()
    return render(request, 'Blog/blog-main.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        pass
    else:
        form_ = forms.New_Post()
    return render(request, 'Blog/add-post.html', {'form': form_})
