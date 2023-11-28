from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =('image', 'title', 'type', 'brand', 'size', 'more_sizing', 'about', 'contact_info') #update for image

class PosterForm(ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
