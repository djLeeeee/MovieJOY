from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie, Review
from .review import ReviewListSerializer

User = get_user_model()

# Movie 
class MovieSerializer(serializers.ModelSerializer):

    class CustomReviewSerializer(ReviewListSerializer):

        class Meta:
            model = Review
            fields = '__all__'

    reviews = CustomReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('tmdb_movie_id', 'poster_path', 'name', 'vote_average',)
