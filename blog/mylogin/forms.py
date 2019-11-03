from django import forms
from django.contrib.auth.models import User


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']



class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',
                 'first_name', 'last_name']