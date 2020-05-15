from django.shortcuts import render

from .models import Movies

# Create your views here.
def home(request):
    movies = Movies.objects.all()

    frontend = {'movies': movies}
    return render(request, 'movie/home.html', frontend)


def search(request):
    if request.method == 'POST':
        search = request.POST.get('search-movie')
        movies = Movies.objects.filter(movie__contains=search)
    else:
        movies = Movies.objects.all()

    frontend = {'movies': movies}
    return render(request, 'movie/home.html', frontend)