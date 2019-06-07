from django.urls import path
from .views import HomeTemplate
urlpatterns = [
    path('',HomeTemplate.as_view(),name='home')
]