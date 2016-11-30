from django import forms
from django.contrib.auth.models import User
from .models import blogmod

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BlogForm(forms.ModelForm):

    class Meta:
        model = blogmod
        fields = ['title', 'blog_text', 'date']