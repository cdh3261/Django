from django.db import models
from django.core.validators import EmailValidator,MinValueValidator

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


class Person(models.Model):
    last_name = models.TextField()
    email = models.CharField(max_length=50,validators=[EmailValidator(message='이메일 형식을 넣어주세요.')])
    age = models.IntegerField(validators=[MinValueValidator(20, message='미성년자는 가입할 수 없습니다.')])