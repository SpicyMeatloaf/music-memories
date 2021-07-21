from django.db import models
from django.urls import reverse

# Create your models here.


class Music(models.Model):
    date_created = models.DateField()
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        if (self.song):
            return self.song
        elif (self.album):
            return self.album
        else:
            return self.artist

class Photo(models.Model):
    url = models.CharField(max_length=200)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for music_id: {self.music_id} @{self.url}"