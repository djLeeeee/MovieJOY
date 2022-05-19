from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Avg
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Review, Genre
from .serializers.movie import MovieSerializer, MovieListSerializer
from .serializers.review import ReviewSerializer, ReviewListSerializer
from .serializers.genre import GenreSerializer

# Create your views here.
@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, tmdb_movie_id):
    if not Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():
        movie = Movie(tmdb_movie_id=tmdb_movie_id)
        movie.save()
    movie = Movie.objects.filter(
        tmdb_movie_id=tmdb_movie_id
    ).annotate(
        reviews_score_average=Avg('reviews__score')
    )[0]
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_like(request, tmdb_movie_id):
    movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            movie.dislike_users.add(request.user)
        elif movie.dislike_users.filter(pk=request.user.pk).exists():
            movie.dislike_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def reviews_c(request, tmdb_movie_id):
    movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def review_ud(request, tmdb_movie_id, review_pk):
    movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        elif request.method == 'DELETE':
            review.delete()
    reviews = movie.reviews.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def genre_like(request, tmdb_genre_id):
    genre = get_object_or_404(Genre, tmdb_genre_id=tmdb_genre_id)
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if genre.like_users.filter(pk=request.user.pk).exists():
            genre.like_users.remove(request.user)
        else:
            genre.like_users.add(request.user)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)
