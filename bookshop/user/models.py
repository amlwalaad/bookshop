from django.db import models
from django.forms import Form
from books.models import books
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class borrowred_books(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user id')
    book_id = models.ForeignKey(books, on_delete=models.CASCADE, db_column='book title')
    data_borrowe = models.DateTimeField(auto_now_add=True, db_column='the time of borrowe')
    data_return = models.DateField(db_column="return data")

    def __str__(self):
        stingg = str(self.book_id)
        return stingg


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

