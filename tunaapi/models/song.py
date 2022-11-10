from django.db import models


class Song(models.Model):

    title = models.CharField(max_length=50)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name='songs')
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, related_name='song_genre')
    album = models.CharField(max_length=50)
    length = models.IntegerField(blank=False, null=False)