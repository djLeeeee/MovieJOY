import requests
import json

BASE_URL = 'https://api.themoviedb.org/3'
API_KEY = '52962731aacacff3f5f9da655947bff6'


def get_trailer():
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
        'page': 0
    }

    end_page = 5
    movies = []
    for _ in range(end_page):
        params['page'] += 1
        movies += requests.get(BASE_URL + path, params=params).json()['results']
    print(movies)
    movies_result = {'data': []}
    for movie in movies:
        trailer_path = ''
        movie_id = movie['id']
        path = f'/movie/{movie_id}/videos'
        trailers = requests.get(BASE_URL + path, params=params).json()['results']
        for trailer in trailers:
            if trailer["site"] == "YouTube":
                trailer_path = trailer["key"]
                if trailer["official"]:
                    break
        if trailer_path:
            movie["trailer_path"] = trailer_path
            movies_result['data'].append(movie)
        else:
            print(movie)

    file_path = './movies.json'

    with open(file_path, 'w', encoding='UTF-8') as outfile:
        json.dump(movies_result, outfile, indent=4, ensure_ascii=False)


def get_genre_movie_list_to_fixture():
    path = '/genre/movie/list'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()
    result = []
    pk = 0
    for genre in response['genres']:
        pk += 1
        genre_info = {"model": "movies.genre", "pk": pk,
                      "fields": {
                          "tmdb_genre_id": genre['id'],
                          "name": genre['name'],
                          "like_users": []
                      }}
        result.append(genre_info)
    file_path = './genres.json'
    with open(file_path, 'w', encoding='UTF-8') as outfile:
        json.dump(result, outfile, indent=4, ensure_ascii=False)


def get_upcoming():
    path = '/movie/upcoming'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
    }


def now_playing_movie():
    path = '/movie/now_playing'
    params = {
        'api_key': API_KEY,
        'region': 'KR',
        'language': 'ko',
    }
    response = requests.get(BASE_URL + path, params=params).json()['results']
    print(response)


now_playing_movie()