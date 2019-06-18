from django.db.models import QuerySet, Sum, Count, FloatField


class MovieQueryset(QuerySet):
    def get_by_year(self, year=None):
        if year:
            return self.filter(release_date__year=year)
        else:
            return self


class MovieRateQueryset(QuerySet):
    def get_best_rated(self):
        return self.values('movie').annotate(
         rate=Sum('rate') / Count('movie', output_field=FloatField())).order_by('-rate')

    def get_rated(self,pk):
        return self.values('movie').annotate(
         rate=Sum('rate') / Count('movie', output_field=FloatField())).filter(movie=pk)
    def get_for_movie(self, movie):
        return self.filter(movie=movie)

    def get_rate_for_movie(self, movie):
        return self.get_for_movie(movie).get_best_rated()