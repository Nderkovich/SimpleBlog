from django import forms
from .models import Post


class Add_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'is_shared']