from django.forms import ModelForm
#from django import forms
from .models import *


#create class for project form

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =('image', 'title', 'type', 'brand', 'size', 'more_sizing', 'about', 'contact_info') #update for image
