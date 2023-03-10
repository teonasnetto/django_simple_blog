from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
import re
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator, has_role_decorator
from rolepermissions.roles import assign_role, remove_role
from rolepermissions.permissions import revoke_permission, grant_permission

@login_required
def blog(request):
    return render(request, 'blog/blog.html', {})

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    links = re.findall('(https?://[^\s]+)', post.text)
    if len(links) > 0:
        link = links[0]
    else:
        link = None
    return render(request, 'blog/post_detail.html', {'post': post, 'link': link})

@login_required
@has_permission_decorator('can_publish')
def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.updated_at = timezone.now()
             post.publish()
             return redirect('blog:post_detail', slug=post.slug)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@has_permission_decorator('can_edit')
def post_edit(request, slug):
     post = get_object_or_404(Post, slug=slug)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.updated_at = timezone.now()
             post.save()
             return redirect('blog:post_detail', slug=post.slug)
     else:
         form = PostForm(instance=post)
     return render(request, 'blog/post_edit.html', {'form': form})