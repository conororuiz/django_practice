import datetime
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
import json
from movies.models import *
import os


class Command(BaseCommand):
    help = 'fetch movies from OMDB API'

    def add_arguments(self, parser):
        # positional argument
        parser.add_argument('title', type=str)

        # kwargs like arguments
        parser.add_argument('-s', '--search', action='store_true', default=False)

    def handle(self, *args, **options):
        search = options['search']
        title = options['title']
        good=False
        try:
            int(title)
        except:
            good=True
        if good:
            url="http://www.omdbapi.com/?s={}&apikey=c3940747".format(title)
            results = requests.get(url)
            movie = results.json()
            movie= movie['Search']
            ids=[]
            for i in movie:
                ids.append(i['imdbID'])
            for i in range(len(ids)):
                  url="http://www.omdbapi.com/?i={}&apikey=c3940747".format(ids[i])
                  results = requests.get(url)
                  results=results.json()
                  if results['Type'] == "movie":
                      movie_title=results['Title']
                      try:
                          duration=results['Runtime']
                          duration=duration.split()
                          duration=int(duration[0])
                      except:
                          duration=123
                      detail=results['Plot']
                      genre=results['Genre']
                      genre=genre.split()
                      genre=genre[0]
                      language=results['Language']
                      language=language.split()
                      language=language[0]
                      country=results['Country']
                      response=results["Poster"]
                      year=results['Released']
                      year=year.split()
                      year=year[len(year)-1]
                      ad="({})".format(year)
                      movie_title=movie_title+year
                      dir=str(i)
                      ext=response.split(".")
                      ext=ext[len(ext)-1]
                      poster_name=''
                      date_release = results['Released']
                      trailer=results['Website']
                      director=results['Director']
                      director=director.split(',')
                      director=director[0]
                      actors=results['Actors']
                      actors=actors.split()
                      actors=actors[0]
                      if date_release=='N/A':
                          date_release = datetime.datetime.strptime('01 jun 1999', '%d %b %Y')

                      else:
                          date_release = datetime.datetime.strptime(date_release, '%d %b %Y')

                      if(ext=="N/A"):
                          pass
                      else:
                          try:
                           os.mkdir(settings.MEDIA_ROOT+"/movie/"+movie_title+dir)
                          except:
                              print("la pelicula ya existe")
                          poster_name=settings.MEDIA_ROOT+"/movie/"+movie_title+dir+"/"+movie_title+"."+ext
                          f = open(poster_name, "wb")
                          try:
                            response = requests.get(response)
                            f.write(response.content)
                          except:
                            poster_name="prueba"
                          f.close()
                          poster_name="movie/"+movie_title+dir+"/"+movie_title+"."+ext
                          actors=Actor.objects.create(name=Actor,age=0)
                          director=MovieDirector.objects.create(name=director,age=0)
                          Movie.objects.create(title=movie_title, duration=duration, poster=poster_name, detail=detail,
                                               genre=genre, original_language=language,
                                               country=country, release_date=date_release, year=year,
                                               classification='N/A', trailer_url=trailer,
                                               directors=director, actors=actors, rating=0.0)


        print("success")