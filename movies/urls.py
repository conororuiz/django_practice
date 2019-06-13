from django.urls import path
from .views import *
urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('home',HomeTemplate.as_view(),name='home'),
    path('shearch/<str:slug>',MovieDetailView.as_view(),name='shearch'),
    path('movies',HomeTemplate.as_view(),name='movies'),
    path('create_movie',MovieView.as_view(),name='create'),
    path('rate',MovieRateView.as_view(),name='rate')
]