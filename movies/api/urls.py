from django.urls import path

from movies.api.viewsets import AccountViewSet

urlpatterns = [
    path('movie/', AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list-actions'),
    path('movie/<int:pk>/',
          AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}),
         name='movie-detail-actions'),
]