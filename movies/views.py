from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm, ReviewForm
from .models import Movie, Review
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



# Vista para mostrar todas las películas
def list_movies(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/movie_list.html', {'page_obj': page_obj})

# Vista para detalle de una película
def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    reviews = movie.reviews.all()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews
        })

@login_required
def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        form = MovieForm()
    return render(request, 'movies/create_movie.html', {'form': form})

# Crear una nueva reseña para una película
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()

    # Pass 'movie' to the template context
    return render(request, 'movies/create_review.html', {'form': form, 'movie': movie})

# Actualizar una película existente
@login_required
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/update_movie.html', {'form': form, 'movie': movie})

# Eliminar una película
@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "DELETE":
        movie.delete()
        return JsonResponse({"message": "Movie deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=405)

# Eliminar una reseña
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'DELETE':
        review.delete()
        return JsonResponse({"message": "Review deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=405)