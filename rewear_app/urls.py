from django.urls import path, re_path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
#Added in Sprint1
path('posts/', views.PostListView.as_view(), name= 'posts'),
path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
#Add to path later so that these are linked with a user
path('create_post/', views.createPost, name='create_post'),
path('update_post/<int:post_id>/', views.updatePost, name='update_post'),
path('delete_post/<int:post_id>/', views.deletePost, name='delete_post'),

]

