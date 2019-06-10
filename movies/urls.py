from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeTemplate.as_view(),name='home'),
    path('shearch/<int:pk>',MovieDetails.as_view(),name='shearch')
]