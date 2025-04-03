from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment

def Home(request):
    post = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': post})

@login_required
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("Home")
        else:
            return HttpResponse("The form content is incorrect, please fill it out again.")
    else:
        post_form = PostForm()
        return render(request, "blog/create_blog.html", {"form":post_form})
