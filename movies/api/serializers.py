from django.urls import reverse
from django.views import generic
from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.serializers import ModelSerializer

from movies.models import MovieRate, Movie


class MovieSerializer(ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='api-movies:movie-detail', lookup_field='pk')

    class Meta:
        model = Movie
        fields = '__all__'
    permission_classes = [DjangoModelPermissions, ]



class MovieRateSerializer(ModelSerializer):
    pk = serializers.IntegerField(source='id', read_only=True)
    users = serializers.StringRelatedField()
    movie = MovieSerializer(read_only=True)
    comment = serializers.CharField()

    class Meta:
        model = MovieRate
        fields = ('movie', 'users', 'comment', 'rate', 'pk')

