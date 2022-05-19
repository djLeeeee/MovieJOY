from email.policy import default
from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie
from .review import ReviewSerializer

User = get_user_model()

# Movie 
class MovieSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_score_average = serializers.FloatField(default=0)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
