from django.urls import include, path, re_path
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
path('poster/<int:pk>', views.PosterDetailView.as_view(), name='poster-detail'),
#Add to path later so that these are linked with a user



path('user/<int:user_id>/create_post/', views.createPost, name='create_post'),
path('update_post/<int:post_id>/', views.updatePost, name='update_post'),
path('delete_post/<int:post_id>/', views.deletePost, name='delete_post'),

path('accounts/', include('django.contrib.auth.urls')),
path('accounts/register/', views.registerPage, name= 'register_page'),
path('user/', views.userPage, name = 'user_page'),
path('accounts/profile/', views.profilePage, name = 'profile'),
path('poster/<int:pk>', views.PosterDetailView.as_view(), name='poster-detail'),
]


"""
path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
path('portfolio/<int:portfolio_id>/update_project/<int:project_id>/', views.updateProject, name='update_project'),
path('portfolio/<int:portfolio_id>/delete_project/<int:project_id>/', views.deleteProject, name='delete_project'),
"""

