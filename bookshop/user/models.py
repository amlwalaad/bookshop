from django.db import models
from django.forms import Form
from books.models import books
from django.contrib.auth.models import User


# Create your models here.

class borrowred_books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user id')
    book_title = models.ForeignKey(books, on_delete=models.CASCADE, db_column='book title')
    data_borrowe = models.DateTimeField(auto_now_add=True, db_column='the time of borrowe')
    data_return = models.DateField(db_column="return data")
