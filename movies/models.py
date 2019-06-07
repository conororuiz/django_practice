from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class MovieDirector(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Actor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=70)
    duration = models.TimeField()
    year = models.IntegerField()
    poster = models.ImageField()
    detail = models.TextField()
    trailer_url = models.URLField()
    directors = models.ForeignKey(MovieDirector,on_delete=models.CASCADE)
    actors = models.ForeignKey(Actor,on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)
    rating = models.IntegerField()
    original_language = models.CharField(max_length=20)
    release_date = models.DateField()
    country = models.CharField(max_length=20)


class MovieRate(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
