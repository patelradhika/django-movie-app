from django.shortcuts import render

from .models import Movies

# Create your views here.
def home(request):
    movies = Movies.objects.all()

    frontend = {'movies': movies}
    return render(request, 'movie/base.html', frontend)