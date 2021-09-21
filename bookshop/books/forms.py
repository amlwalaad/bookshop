from django.forms import ModelForm
from books.models import books


class form_books(ModelForm):
    class Meta:
        model = books
        fields = {'title','author','summary','image','types','price','available'}


