from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie, Review
from .review import ReviewSerializer

User = get_user_model()

# Movie 
class MovieSerializer(serializers.ModelSerializer):

    class CustomReviewSerializer(ReviewSerializer):

        class Meta:
            model = Review
            fields = ('id', 'content', 'score', 'user')

    reviews = CustomReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'tmdb_movie_id', 'poster_path', 'name', 'vote_average',)
