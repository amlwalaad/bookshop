from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import users

class form_signup(UserCreationForm):
    # secret = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = {"first_name","last_name","email","username","password1","password2"}


class user_log(ModelForm):
    class Meta:
        model = users
        fields = ['email', 'password']
