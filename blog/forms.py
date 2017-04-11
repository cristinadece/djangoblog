'''
    djangoblog : forms
    Created by muntean on 4/11/17
'''

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)