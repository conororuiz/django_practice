from rest_framework.viewsets import ModelViewSet

from movies.api.serializers import MovieSerializer
from movies.models import Movie


class AccountViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer