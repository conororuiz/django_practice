from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeTemplate.as_view(),name='home'),
    path('shearch/<str:slug>',MovieDetailView.as_view(),name='shearch'),
    path('movies',HomeTemplate.as_view(),name='movies')
]