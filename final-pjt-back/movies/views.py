from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Review, Genre
from .serializers.movie import MovieSerializer, MovieListSerializer
from .serializers.review import ReviewSerializer, ReviewListSerializer
from .serializers.genre import GenreSerializer
import requests
from random import sample

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = '52962731aacacff3f5f9da655947bff6'
minimum_movie_nums = 12

# Create your views here.
@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, tmdb_movie_id):
    if Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():
        movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)
    else:
        movie = update_movie_db(tmdb_movie_id)
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
        if Review.objects.filter(user=request.user).filter(movie=movie).exists():
            review = get_object_or_404(Review, user=request.user, movie=movie)
            review.delete()
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


@api_view(['GET'])
def recommend_genre_movie(request, tmdb_genre_id):
    genre = get_object_or_404(Genre, tmdb_genre_id=tmdb_genre_id)
    movies = Movie.objects.filter(genres__in=[genre.pk]).filter(~Q(dislike_users__in=[request.user.pk])).order_by('?')
    page = Movie.objects.count() // 20
    while movies.count() < minimum_movie_nums:
        page += 1
        update_movies_db(page)
        movies = Movie.objects.filter(genres__in=[genre.pk]).filter(~Q(dislike_users__in=[request.user.pk])).order_by('?')
    serializer = MovieListSerializer(movies[:minimum_movie_nums], many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommend_tmdb(request):
    user = request.user
    page = 0
    movies = []
    while len(movies) < minimum_movie_nums:
        page += 1
        response = update_movies_db(page)
        for movie in response:
            if user.dislike_movies.filter(pk=movie.pk).exists():
                pass
            else:
                movies.append(movie)
    serializer = MovieListSerializer(sample(movies, minimum_movie_nums), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def upcoming_movie(request):
    path = '/movie/upcoming'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()['results']
    movies = [update_movie_by_json(movie_info) for movie_info in response]
    serializer = MovieListSerializer(sample(movies, min(minimum_movie_nums, len(movies))), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing_movie(request):
    path = '/movie/now_playing'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()['results']
    movies = [update_movie_by_json(movie_info) for movie_info in response]
    serializer = MovieListSerializer(sample(movies, min(minimum_movie_nums, len(movies))), many=True)
    return Response(serializer.data)


def update_movies_db(page):
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
        'page': page,
    }
    movies = []
    response = requests.get(BASE_URL + path, params=params).json()['results']
    for movie_info in response:
        movie = update_movie_by_json(movie_info)
        movies.append(movie)
    return movies


def update_movie_db(tmdb_movie_id):
    path = f'/movie/{tmdb_movie_id}'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()
    return update_movie_by_json(response)


def update_movie_by_json(movie_info):
    tmdb_movie_id = movie_info['id']
    name = movie_info['title']
    poster_path = movie_info['poster_path']
    vote_average = movie_info['vote_average']
    overview = movie_info['overview']
    if not Movie.objects.filter(tmdb_movie_id=tmdb_movie_id).exists():
        movie = Movie(
            tmdb_movie_id=tmdb_movie_id,
            name=name,
            poster_path=poster_path,
            vote_average=vote_average,
            overview=overview
        )
        movie.save()
        if movie_info.get('genre_ids'):
            genres = movie_info['genre_ids']
            for genre_id in genres:
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)
        elif movie_info.get('genres'):
            genres = movie_info['genres']
            for genre in genres:
                genre_id = genre['id']
                genre = get_object_or_404(Genre, tmdb_genre_id=genre_id)
                movie.genres.add(genre)
    else:
        movie = get_object_or_404(Movie, tmdb_movie_id=tmdb_movie_id)
    return movie
