from django.urls import path
from .views import *
urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('home',HomeTemplate.as_view(),name='home'),
    path('shearch/<str:slug>',DetailMovieView.as_view(),name='search'),
    path('home/',HomeTemplate.as_view(),name='movies'),
    path('create_movie',InsertMovies.as_view(),name='create'),
    path('rate/<slug>',MovieRateView.as_view(), name = 'rate'),
    path('movie/', MovieListView.as_view(), name='drf-movie-list'),
    path('movie/<slug>/', MovieDetailView.as_view(), name='drf-movie-detail'),
    path('movierate/', MovieRateListView.as_view(), name='drf-movierate-list'),
    path('movierate/<int:pk>/', MovieRateDetailView.as_view(), name='drf-movierate-detail'),
    path('logout',LogOutView.as_view(), name='logout'),
    path('suggests',SuggestsView.as_view(), name='suggests'),
    path('movies_api/', HomeApiView.as_view(), name='home-api'),
    path('detail_movie/<movie>/', DetailMovie.as_view(), name='detail-api'),

]