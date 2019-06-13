from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView ,DetailView , View
from movies.models import *


class HomeTemplate(ListView):

    def get(self,request, *args, **kwargs):
            movie = Movie.objects.all()
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
        rate =rate[0]
        data.update({'rate':rate })
        return data

""""
class MovieDetails(View):
    def get(self,request, pk):
        pel=int(pk)
        movie=Movie.objects.get(id=pel)
        rate=MovieRate.objects.get_rated(pel)
        context={'movies':movie,'rate':rate}
        return render(request,'shearch_template.html',context) """