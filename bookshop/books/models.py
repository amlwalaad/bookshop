from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=100)
    id=models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', blank=True )
    price = models.FloatField()
    types = models.CharField(max_length=10, choices=[
        ('math', 'math'), ('hiostry', 'hiostry'), ('novel', 'novel'), ('science', 'science')
    ])
    summary=models.CharField(max_length=9999)
    available = models.BooleanField()

    def __str__(self):
        return self.title

