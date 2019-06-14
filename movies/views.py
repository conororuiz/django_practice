from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, FormView, CreateView

from movies.forms import MovieForm, MovieRateForm
from movies.models import *


class HomeTemplate(ListView):
    def get(self,request, *args, **kwargs):
            movie = Movie.objects.all().order_by('-id')[:10]
            best_movie = MovieRate.objects.get_best_rated().first()
            best_movie_rate=Movie.objects.get(pk=best_movie.get('movie'))
            rate = best_movie['rate']
            if self.request.GET.get('q') != None:
               return self.shearchmovie(request)
            contex = {'movies': movie,'best_movie': best_movie_rate , 'movie_rate':rate, }
            return render(request,'index.html', contex)

    def shearchmovie(self,request):
            busqueda = self.request.GET.get('q')
            num = 0
            try:
                num = int(busqueda)
            except:
                pass
            if busqueda == None or busqueda == "":
                movie = Movie.objects.all()
                contex = {'movies': movie}
            elif Movie.objects.filter(title__icontains=busqueda):
                movie = Movie.objects.filter(title__icontains=busqueda)
                contex = {'movies': movie, }
            elif Movie.objects.filter(classification__icontains=busqueda):
                movie = Movie.objects.filter(classification__icontains=busqueda)
                contex = {'movies': movie}
            elif Movie.objects.filter(genre__icontains=busqueda):
                movie = Movie.objects.filter(genre__icontains=busqueda)
                contex = {'movies': movie}
            elif Movie.objects.filter(actors__name__icontains=busqueda):
                movie = Movie.objects.filter(actors__name__icontains=busqueda)
                contex = {'movies': movie}
            elif Movie.objects.filter(directors__name__icontains=busqueda):
                movie = Movie.objects.filter(directors__name__icontains=busqueda)
                contex = {'movies': movie}
            elif Movie.objects.filter(year=num):
                movie = Movie.objects.filter(year=num)
                contex = {'movies': movie}
            else:
                contex = {'movies': 'no se encontraron conicidencias'}
            return render(request,'movies.html', contex)

class MovieDetailView(LoginRequiredMixin, DetailView):
    queryset = Movie.objects.all()
    template_name = 'shearch_template.html'
    slug_field = 'slug'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        data = super(MovieDetailView, self).get_context_data(**kwargs)
        rate=MovieRate.objects.get_rated(self.get_object().id)
        if rate:
          rate =rate[0]
        else:
          rate=float(0.0)
        data.update({'rate':rate })
        return data

class Login(LoginView):
     template_name = 'login.html'


class MovieView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'create_movie.html'
    success_url = 'home'

class MovieRateView(CreateView):
    model = MovieRate
    form_class = MovieRateForm
    template_name = 'rate.html'
    success_url = 'home'