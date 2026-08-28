from db import get_watched_ids, get_genre_scores

def score_movie(movie, genre_prefs):
    base_score = movie["vote_average"]  # 0-10 from TMDB
    genre_bonus = 0
    matched = 0
    for g in movie.get("genre_ids", []):
        if g in genre_prefs:
            genre_bonus += genre_prefs[g]
            matched += 1
    if matched:
        genre_bonus = (genre_bonus / matched) - 5  # center around 0
    return base_score + genre_bonus * 1.5  # weight your taste more than raw rating

def recommend(movies, top_n=5):
    watched = get_watched_ids()
    genre_prefs = get_genre_scores()  # {} on first run — falls back to pure TMDB rating

    candidates = [m for m in movies if m["id"] not in watched]
    candidates.sort(key=lambda m: score_movie(m, genre_prefs), reverse=True)
    return candidates[:top_n]