import requests
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies(pages=3):
    """Pulls a pool of popular/well-rated movies to pick from."""
    movies = []
    for page in range(1, pages + 1):
        resp = requests.get(f"{BASE_URL}/discover/movie", params={
            "api_key": TMDB_API_KEY,
            "sort_by": "popularity.desc",
            "vote_average.gte": 6.0,
            "vote_count.gte": 200,
            "page": page
        })
        resp.raise_for_status()
        movies.extend(resp.json()["results"])
    return movies

def get_genre_map():
    resp = requests.get(f"{BASE_URL}/genre/movie/list", params={"api_key": TMDB_API_KEY})
    resp.raise_for_status()
    return {g["id"]: g["name"] for g in resp.json()["genres"]}