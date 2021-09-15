from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import users


# class user_reg(forms.ModelForm):
#     password_confirm = forms.CharField(widget=forms.PasswordInput, label="confirm password")
#
#     class Meta:
#         model = users
#         widgets = {
#             'password': forms.PasswordInput(),
#             'type': forms.Select(choices=[
#                 ('a', 'admin'),
#                 ('u', '')
#             ]),
#         }
#
#         fields = {"fullname", "id", "email", "type", "password"}

class form_signup(UserCreationForm):
    # secret = forms.CharField(max_length=100,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = {"first_name","last_name","email"}


class user_log(forms.ModelForm):
    class Meta:
        model = users
        fields = ['email', 'password']
