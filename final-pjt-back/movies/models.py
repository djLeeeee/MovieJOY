from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    tmdb_genre_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

    def __str__(self) -> str:
        return self.name + '/' + str(self.tmdb_genre_id)


class Movie(models.Model):
    tmdb_movie_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    vote_average = models.FloatField(default=0)
    overview = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')

    def __str__(self) -> str:
        return self.name + '/' + str(self.tmdb_movie_id)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(max_length=100)
    score = models.IntegerField(
        default = 0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
