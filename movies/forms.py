from movies.models import *
from  django.core.exceptions import ValidationError
from django import forms

class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie
        fields='__all__'

class MovieRateForm(forms.ModelForm):
    rate = forms.IntegerField()

    class Meta:
        model = MovieRate
        fields = ('rate', 'comment')

    def __init__(self, user,movie, *args, **kwargs):
        self.users = user
        self.movie = movie
        super(MovieRateForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(MovieRateForm, self).clean()
        movie = data.get('movie')
        if MovieRate.objects.filter(users=self.users, movie=movie).exists():
            raise ValidationError(f'Movie rate with user {self.users.username} and movie {movie.title} already exists')
        return data

    def save(self, commit=True):
        instance = super(MovieRateForm, self).save(commit=False)
        instance.users = self.users
        instance.movie = self.movie
        instance.save()
        return instance


class InsertMovieForm(forms.Form):
     name=forms.CharField(max_length=100)
