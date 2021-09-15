from django.contrib import admin
from user.models import users ,borrowred_books
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(users)
admin.site.register(borrowred_books)