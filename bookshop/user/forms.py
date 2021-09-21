from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import borrowred_books


class form_signup(UserCreationForm):
    class Meta:
        model = User
        fields = {"id","first_name", "last_name", "email", "username", "password1", "password2"}

class form_borrowe(ModelForm):
    class Meta:
        model = borrowred_books
        fields="__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
