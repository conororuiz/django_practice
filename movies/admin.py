from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(MovieDirector)
admin.site.register(MovieRate)
admin.site.register(Actor)

