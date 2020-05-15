from django.db import models

# Create your models here.
class Movies(models.Model):

    __tablename__ = 'movies'

    movie = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    pic = models.URLField(max_length=500, default="https://www.prokerala.com/movies/assets/img/no-poster-available.jpg")
    added_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.movie

    class Meta:
        verbose_name_plural = "Movies"