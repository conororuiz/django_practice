import django_filters

from movies.models import Movie


class MovieFilter(django_filters.FilterSet):
    actors = django_filters.CharFilter(field_name='actors', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['actors', 'title', 'year', 'genre',]
