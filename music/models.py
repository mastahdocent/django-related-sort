from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    order = models.CharField(max_length=255)

    def get_tracks(self):
        tracks = {str(i.id): i for i in Track.objects.filter(album=self.id)}
        order_list = self.order.split(',')
        return [tracks[key] for key in order_list if key in tracks.keys()]


class Track(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='+')
    title = models.CharField(max_length=255)
