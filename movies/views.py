from django.shortcuts import render
from django.views.generic import ListView ,View
from movies.models import *


class HomeTemplate(ListView):

    def get(self,request, *args, **kwargs):
        busqueda = self.request.GET.get('q')
        num=0
        try:
            num=int(busqueda)
        except:
           pass
        if busqueda == None or busqueda=="":
            movie = Movie.objects.all()
            contex = {'movies': movie, }
        elif Movie.objects.filter(title__icontains=busqueda):
            movie=Movie.objects.filter(title__icontains=busqueda)
            contex = {'movies': movie, }
        elif Movie.objects.filter(classification__icontains=busqueda):
            movie = Movie.objects.filter(classification__icontains=busqueda)
            contex = {'movies': movie }
        elif Movie.objects.filter(genre__icontains=busqueda):
            movie= Movie.objects.filter(genre__icontains=busqueda)
            contex = {'movies': movie}
        elif Movie.objects.filter(actors__name__icontains=busqueda):
            movie= Movie.objects.filter(genre__name__icontains=busqueda)
            contex = {'movies': movie}
        elif Movie.objects.filter(year=num):
            movie= Movie.objects.filter(year=num)
            contex = {'movies': movie}
        else:
            contex={'movies': 'no se encontraron conicidencias' }
        return render(request,'index.html',contex)

class MovieDetails(View):
    def get(self,request, pk):
        pel=int(pk)
        movie=Movie.objects.get(id=pel)
        context={'movies':movie}
        return render(request,'shearch_template.html',context)
