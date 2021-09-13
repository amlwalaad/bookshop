from django.db import models
from books.models import books
# Create your models here.
class users(models.Model):
    fullname=models.CharField(max_length=100 , db_column='full name')
    id=models.IntegerField(unique=True , primary_key=True)
    email=models.EmailField()
    type=models.CharField(max_length=5, choices=[
        ('admin','admin'),('user','user')
    ])
    password =models.CharField(max_length=100)
    def __str__(self):
        return self.email
class borrowred_books(models.Model):
    user_id=models.ForeignKey(users , on_delete=models.CASCADE , db_column='user id')
    book_title=models.ForeignKey(books,on_delete=models.CASCADE ,db_column='book title')
    data_borrowe=models.DateTimeField(auto_now_add=True ,db_column='the time of borrowe')
    data_return=models.DateField(db_column="return data")