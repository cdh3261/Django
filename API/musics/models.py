from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content