from django.forms import forms
from django.forms import ModelForm
from user.models import users

class user_register(ModelForm):
    class Meta :
        model=users
        fields= "__all__"
class user_log(ModelForm):
    class Meta :
        model=users
        fields=['email','password']
