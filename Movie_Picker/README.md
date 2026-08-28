# Movie Picker

A personal desktop application built with Python that recommends a movie to watch today. It pulls movie data from The Movie Database (TMDB) API and learns your taste over time based on the movies you mark as watched and rate.

## Features

- Suggests a movie to watch based on TMDB ratings, popularity, and genre
- Learns from your ratings over time and adjusts future recommendations accordingly
- "Suggest another" cycles through different options instead of repeating the same one
- Tracks watch history and ratings locally in a SQLite database
- Simple desktop GUI built with Tkinter (no extra GUI framework required)

## Tech Stack

- Python 3
- Tkinter (GUI)
- SQLite (local storage for watch history and ratings)
- TMDB API (movie data)
- requests (API calls)
- python-dotenv (environment variable management)

## Project Structure

```
Movie_Picker/
├── main.py            # GUI entry point
├── tmdb_client.py      # TMDB API wrapper
├── db.py                # Local SQLite database logic
├── recommender.py       # Recommendation and scoring logic
├── config.py             # Loads API key from environment
├── .env.example           # Template for required environment variables
└── movies.db               # Local database (created automatically, not tracked in git)
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/datanhbo08/Small_Project_Weekend.git
   cd Small_Project_Weekend/Movie_Picker
   ```

2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```

3. Get a free TMDB API key:
   - Create an account at https://www.themoviedb.org/
   - Go to Settings, then API, then request a Developer API key
   - Copy your API key (v3)

4. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Add your TMDB API key:
     ```
     TMDB_API_KEY=your_actual_key_here
     ```

5. Run the app:
   ```
   python main.py
   ```

## How It Works

On first run, the app pulls a pool of popular, well-rated movies from TMDB and recommends the top-scoring one. As you mark movies watched and rate them, the app builds a local profile of which genres you tend to rate highly. Future recommendations are then scored using both the TMDB rating and how well each movie's genres match your personal preferences.

## Notes

- This is a personal, non-commercial project built for learning and portfolio purposes.
- `.env` and `movies.db` are excluded from version control since they contain your personal API key and local watch history.
- Movie data is provided by TMDB. This product uses the TMDB API but is not endorsed or certified by TMDB.

## Possible Future Improvements

- Display movie posters
- Add a mood or genre filter before generating a suggestion
- Filter by streaming service availability
- Switch to a more modern GUI framework such as customtkinter