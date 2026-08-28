import sqlite3

DB_PATH = "movies.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            movie_id INTEGER PRIMARY KEY,
            title TEXT,
            genre_ids TEXT,
            user_rating INTEGER,  -- 1-5, NULL if not yet rated
            watched_date TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_to_history(movie_id, title, genre_ids, user_rating=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO history (movie_id, title, genre_ids, user_rating, watched_date)
        VALUES (?, ?, ?, ?, datetime('now'))
    """, (movie_id, title, ",".join(map(str, genre_ids)), user_rating))
    conn.commit()
    conn.close()

def get_watched_ids():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT movie_id FROM history")
    ids = {row[0] for row in c.fetchall()}
    conn.close()
    return ids

def get_genre_scores():
    """Returns {genre_id: avg_rating} based on past ratings."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT genre_ids, user_rating FROM history WHERE user_rating IS NOT NULL")
    rows = c.fetchall()
    conn.close()

    scores = {}
    counts = {}
    for genre_str, rating in rows:
        for g in genre_str.split(","):
            if not g:
                continue
            g = int(g)
            scores[g] = scores.get(g, 0) + rating
            counts[g] = counts.get(g, 0) + 1
    return {g: scores[g] / counts[g] for g in scores}