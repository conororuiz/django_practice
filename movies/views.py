from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core import management
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, FormView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from movies.api.serializers import MovieSerializer, MovieRateSerializer
from movies.forms import MovieForm, MovieRateForm, InsertMovieForm
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

class DetailMovieView(LoginRequiredMixin, DetailView):
    queryset = Movie.objects.all()
    template_name = 'shearch_template.html'
    slug_field = 'slug'
    query_pk_and_slug = False

    def get_context_data(self, **kwargs):
        data = super(DetailMovieView, self).get_context_data(**kwargs)
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
    template_name = 'rate.html'
    form_class = MovieRateForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        return super(MovieRateView, self).form_invalid(form)


    def get_form_kwargs(self):
        kwargs = super(MovieRateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'movie': Movie.objects.get(slug=self.kwargs.get('slug'))})
        return kwargs

class InsertMovies(FormView):
    template_name = 'create_movie.html'
    form_class = InsertMovieForm
    success_url = 'home'

    def form_valid(self, form):
       management.call_command("download",self.request.POST['name'])
       return super().form_valid(form)

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'


class MovieRateListView(ListAPIView):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer


class MovieRateDetailView(RetrieveAPIView):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer

class LogOutView(LogoutView):
    pass




