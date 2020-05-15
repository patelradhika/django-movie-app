from django.db import models

# Create your models here.
class Movies(models.Model):

    __tablename__ = 'movie'

    movie = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=False, null=False)
    pic = models.URLField(max_length=500)

    def __str__(self):
        return self.movie
