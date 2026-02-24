from django.db import models

# Create your models here.
from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200) # e.g., "Annual Sports Day 2026"
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='albums/') # The main card photo
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='school_gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Photo for {self.album.title}"