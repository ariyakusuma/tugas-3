from django.db import models

class MovieList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.TextField(default='')
    rating = models.IntegerField(default=0)
    release_day = models.TextField(default='')
    review = models.TextField(default='')

# Create your models here.
