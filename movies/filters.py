

from movies.models import Movie


def search_movies(busqueda):
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
    return contex