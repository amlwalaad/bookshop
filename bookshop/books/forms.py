from django.forms import ModelForm
from books.models import books


class form_books(ModelForm):
    class Meta:
        model = books
        fields = "__all__"


