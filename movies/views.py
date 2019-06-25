from builtins import super
import secrets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core import management
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, FormView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework import filters, generics
from movies.api.serializers import MovieSerializer, MovieRateSerializer
from movies.filters import MovieFilter
from movies.forms import MovieForm, MovieRateForm, InsertMovieForm
from movies.models import MovieRate, Movie


class HomeTemplate(ListView):
    def get(self,request, *args, **kwargs):
          if Movie.objects.all().order_by('-id')[:10]:
            movie = Movie.objects.all().order_by('-id')[:10]
            if MovieRate.objects.get_best_rated().first():
                best_movie = MovieRate.objects.get_best_rated().first()
                best_movie_rate=Movie.objects.get(pk=best_movie.get('movie'))
                rate = best_movie['rate']
                if self.request.GET.get('title') != None:
                   return self.shearchmovie(request)
                contex = {'movies': movie,'best_movie': best_movie_rate , 'movie_rate':rate, }
                return render(request,'index.html', contex)
            else:
                if self.request.GET.get('title') != None:
                   return self.shearchmovie(request)
                contex = {'movies': movie,}
                return render(request,'index.html', contex)
          else:
              if self.request.GET.get('title') != None:
                  return self.shearchmovie(request)
              contex = {}
              return render(request, 'index.html', contex)

    def shearchmovie(self,request):
        movie_list = Movie.objects.all()
        movie_filter = MovieFilter(request.GET, queryset=movie_list)
        return render(request, 'movies.html',{'movies': movie_filter})


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

     def form_valid(self, form):
         context = super(Login,self).form_valid(form)
         try:
            Token.objects.get(user=self.request.user.pk)
         except:
            Token.objects.create(user=self.request.user)
         return context

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

    def dispatch(self, request, *args, **kwargs):
        try:
          Token.objects.get(user=self.request.user.pk).delete()
        except:
            return redirect('login')
        logout(request)
        return super(LogOutView,self).dispatch(request, *args, **kwargs)
