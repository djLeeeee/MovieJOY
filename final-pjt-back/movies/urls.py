from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list),
    path('<int:tmdb_movie_id>/', views.movie_detail),
    path('<int:tmdb_movie_id>/like/', views.movie_like),
    path('<int:tmdb_movie_id>/reviews/', views.reviews_c),
    path('<int:tmdb_movie_id>/reviews/<int:review_pk>/', views.review_ud),
    path('<int:tmdb_genre_id>/genre/', views.genre_like),
    path('<int:tmdb_genre_id>/recommendation/', views.recommend_genre_movie),
    path('genres/recommendation/',views.recommend_genres),
    path('reviews/recommendation/', views.recommend_reviews),
    path('tmdb/recommendation/', views.recommend_tmdb),
    path('tmdb/upcomming/', views.upcoming_movie),
    path('tmdb/nowplaying/', views.now_playing_movie),
]
