from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
from rewear_app.forms import *
from rewear_app.models import *

# Create your views here.
def index(request):
    active_posts = Post.objects.all().order_by("-id")
    print("active posts", active_posts) #prints in the bash line for debugging
    return render( request, 'rewear_app/index.html', {'active_posts':active_posts})

#Added in sprint 1
class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        # Create a new dictionary with form data
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form without committing to the database
            post = form.save(commit=False)
            # Save to database
            post.save()
            # Redirect back to a page
            return redirect('posts')
        
    context = {'form': form}
    return render(request, 'rewear_app/post_form.html', context)

def updatePost(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # Pass the instance to pre-fill the form
        if form.is_valid():
            form.save()
            # Redirect back to the portfolio detail page
            return redirect('posts')
    else:
        form = PostForm(instance=post)  # Initialize the form with the instance

    context = {'form': form}
    return render(request, 'rewear_app/post_form.html', context)

def deletePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        post.image.delete()
        post.delete()
        return redirect('posts')
    context = {
        'post': post,  # Pass the project object to the template context
    }
    return render(request, 'rewear_app/post_delete.html', context)

