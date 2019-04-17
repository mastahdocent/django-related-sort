from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    order = models.CharField(max_length=255)


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=255)
