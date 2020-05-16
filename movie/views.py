from django.contrib import messages
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
        try:
            name = request.POST.get('movie-name')
            rating = int(request.POST.get('movie-rating'))
            pic = request.POST.get('movie-pic') or "https://www.prokerala.com/movies/assets/img/no-poster-available.jpg"
            desc = request.POST.get('movie-desc') or None

            movie = Movies.objects.create(movie=name, rating=rating, pic=pic, desc=desc)
            movie.save()

            messages.success(request, "Successfully added new movie: {}".format(movie.movie))
        
        except ValueError:
            messages.warning(request, "Got error while updating movie: Rating must be a number(1-10)")
            
        except Exception as e:
            messages.warning(request, "Got error while adding new movie: {}".format(e))

        return redirect('/')
    else:
        return redirect('/')


def edit(request, id):
    if request.method == "POST":
        try:
            movie = Movies.objects.get(id=id)

            movie.movie = request.POST.get('name')
            movie.rating = int(request.POST.get('rating'))
            movie.pic = request.POST.get('pic') or movie.pic
            movie.desc = request.POST.get('desc') or None

            movie.save()
            messages.success(request, "Successfully updated movie: {}".format(movie.movie))

        except ValueError:
            messages.warning(request, "Got error while updating movie: Rating must be a number(1-10)")

        except Exception as e:
            messages.warning(request, "Got error while updating movie: {}".format(e))

        return redirect('/')
    else:
        return redirect('/')


def delete(request, id):
    if request.method == 'POST':
        try:
            movie = Movies.objects.get(id=id)
            name = movie.movie
            
            movie.delete()

            messages.success(request, "Successfully deleted movie: {}".format(name))

        except Exception as e:
            messages.warning(request, "Got error while deleting movie: {}".format(e))
        
        return redirect('/')
    else:
        return redirect('/')