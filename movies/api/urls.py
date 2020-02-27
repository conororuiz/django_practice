from django.urls import path
from rest_framework.routers import SimpleRouter
from movies.api.viewsets import MovieViewset, MovieRateViewset

router = SimpleRouter()
router.register('movie', MovieViewset)
router.register('movierate', MovieRateViewset)

urlpatterns = router.urls
