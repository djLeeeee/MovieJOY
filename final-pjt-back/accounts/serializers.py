from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, Review
from .models import SMS_auth


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('tmdb_movie_id', 'name')

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('tmdb_genre_id',)

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('id', 'movie', 'score',)

    like_genres = GenreSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    dislike_movies = MovieSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'nickname', 'like_genres', 'like_movies', 'dislike_movies', 'reviews', 'phone_number')


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = SMS_auth
        fields = '__all__'
