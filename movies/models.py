from builtins import super

from django.contrib.auth import get_user_model
from django.db import models
from movies.queryset import MovieQueryset, MovieRateQueryset
from django.utils.text import slugify

User = get_user_model()

class MovieDirector(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField(null=True)
    year = models.IntegerField()
    poster = models.ImageField(max_length=200)
    detail = models.TextField()
    classification = models.CharField(max_length=5,choices=[("A","para todo publico"),("B","12 años en adelante"),("B15","15 años en adelante"),("C","18 años en adelante"),("D","para adultos")])
    trailer_url = models.URLField()
    directors = models.ForeignKey(MovieDirector,on_delete=models.CASCADE)
    actors = models.ForeignKey(Actor,on_delete=models.CASCADE)
    genre = models.CharField(max_length=100 , default=None)
    rating = models.FloatField()
    original_language = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    country = models.CharField(max_length=100)
    slug=models.CharField(max_length=200 , null=True , blank=True)

    def __str__(self):
        return self.title


class MovieRate(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    users = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    rate = models.FloatField(default=0.0)
    comment = models.TextField()


    objects = MovieRateQueryset.as_manager()

    class Meta:
        unique_together = ('users', 'movie')
        permissions = (
            ('can_vote_two_times', 'Can vote two times'),
        )

    def __int__(self):
        return self.users

class Token(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    token=models.CharField(max_length=80)



class Suggests(models.Model):
    title = models.CharField(max_length=100)

