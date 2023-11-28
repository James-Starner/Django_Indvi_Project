from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin #might need laterslide 13

from django.views import generic
from django.contrib.auth.models import Group
from rewear_app.forms import *
from rewear_app.models import *


# Create your views here.
def index(request):
    active_posts = Post.objects.all().order_by("-id")
    print("active posts", active_posts) #prints in the bash line for debugging
    return render( request, 'rewear_app/index.html', {'active_posts':active_posts})

#Added in sprint 1
class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PosterDetailView(generic.DetailView):
    model = Poster


"""
@login_required(login_url='login')
@allowed_users(allowed_roles=['activeUser']) #chnage this
"""
def createPost(request, user_id):
    form = PostForm()

    if request.method == 'POST':
        # Create a new dictionary with form data
        post_data = request.POST.copy()
        post_data['user'] = user_id

        form = PostForm(post_data, request.FILES)

        if form.is_valid():
            # Save the form without committing to the database
            post = form.save(commit=False)
            post.user_id = user_id
            post.save()
            # Redirect back to a page
            return redirect('user_page')
        
    context = {'form': form}
    return render(request, 'rewear_app/post_form.html', context)


def updatePost(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # Pass the instance to pre-fill the form
        if form.is_valid():
            form.save()
            # Redirect back to the portfolio detail page
            return redirect('user_page')
    else:
        form = PostForm(instance=post)  # Initialize the form with the instance

    context = {'form': form}
    return render(request, 'rewear_app/post_form.html', context)

def deletePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        post.image.delete()
        post.delete()
        return redirect('user_page')
    context = {
        'post': post,  # Pass the project object to the template context
    }
    return render(request, 'rewear_app/post_delete.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='activeUser')
            user.groups.add(group)
            poster = Poster.objects.create(user=user,)
            poster.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['activeUser']) #chnage this
def userPage(request):
    # Filter posts based on the current user
    post_list = Post.objects.filter(user=request.user)

    context = {'post_list': post_list}
    return render(request, 'rewear_app/user.html', context)

def profilePage(request):
    form = PosterForm()

    if request.method == 'POST':
        # Create a new dictionary with form data
        form = PosterForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form without committing to the database
            post = form.save(commit=False)
            # Save to database
            post.save()
            # Redirect back to a page
            return redirect('index')
        
    context = {'form': form}
    return render(request, 'rewear_app/poster_form.html', context)















