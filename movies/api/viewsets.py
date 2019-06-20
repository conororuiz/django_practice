from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.decorators import action
from rest_framework.response import Response

from movies.api.serializers import MovieSerializer, MovieRateSerializer
from movies.models import Movie, MovieRate


class MovieRateViewset(viewsets.ReadOnlyModelViewSet):
    queryset = MovieRate.objects.all()
    serializer_class = MovieRateSerializer


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_classes = {
        'rate': MovieRateSerializer,
        'default': MovieSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action] if self.action in self.serializer_classes.keys() else \
            self.serializer_classes['default']

    def get_serializer_context(self):
        context = super(MovieViewset, self).get_serializer_context()
        context.update({'request': self.request})
        return context

    @action(methods=['POST'], detail=True)
    def rate(self, request, pk=None):
        obj = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=obj, users=request.user)

        return Response(data=self.get_serializer(serializer.instance).data)
