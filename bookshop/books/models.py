from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', )
    price = models.FloatField()
    types = models.CharField(max_length=10, choices=[
        ('math', 'math'), ('hiostry', 'hiostry'), ('novel', 'novel'), ('science', 'science')
    ])
    available = models.BooleanField()
    num_copy = models.IntegerField()

    def __str__(self):
        return self.title
