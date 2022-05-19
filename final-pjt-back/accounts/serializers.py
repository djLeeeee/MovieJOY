from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, Review

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'tmdb_movie_id',)

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk', 'tmdb_genre_id',)

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'movie', 'score',)

    like_genres = GenreSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    dislike_movies = MovieSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'nickname', 'like_genres', 'like_movies', 'dislike_movies', 'reviews',)
