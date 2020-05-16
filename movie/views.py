from django.shortcuts import render, redirect

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


def create(request):
    if request.method == 'POST':
        name = request.POST.get('movie-name')
        rating = int(request.POST.get('movie-rating'))
        pic = request.POST.get('movie-pic') or "https://www.prokerala.com/movies/assets/img/no-poster-available.jpg"
        desc = request.POST.get('movie-desc') or None

        movie = Movies.objects.create(movie=name, rating=rating, pic=pic, desc=desc)
        movie.save()

        return redirect('/')
    else:
        return redirect('/')


def edit(request, id):
    if request.method == "POST":
        movie = Movies.objects.get(id=id)

        movie.movie = request.POST.get('name')
        movie.rating = int(request.POST.get('rating'))
        movie.pic = request.POST.get('pic') or movie.pic
        movie.desc = request.POST.get('desc') or None

        movie.save()

        return redirect('/')
    else:
        return redirect('/')


def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        
        return redirect('/')
    else:
        return redirect('/')