from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration_ms = models.IntegerField()
    # ... other fields
