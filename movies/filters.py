import django_filters

from movies.models import Movie


class MovieFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre','actors']
