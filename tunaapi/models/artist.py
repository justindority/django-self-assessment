from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False, null=False)
    bio = models.CharField(max_length=100)