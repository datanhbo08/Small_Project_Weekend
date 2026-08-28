import tkinter as tk
from tkinter import messagebox
from db import init_db, add_to_history
from tmdb_client import get_popular_movies, get_genre_map
from recommender import recommend

class MoviePickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("What Should I Watch Today?")
        self.root.geometry("480x420")

        init_db()
        self.genre_map = get_genre_map()
        self.pool = get_popular_movies()
        self.current = None

        tk.Label(root, text="🎬 What Should I Watch Today?", font=("Helvetica", 16, "bold")).pack(pady=15)

        self.title_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=420)
        self.title_label.pack(pady=10)

        self.overview_label = tk.Label(root, text="", wraplength=420, justify="left")
        self.overview_label.pack(pady=10)

        self.genre_label = tk.Label(root, text="", fg="gray")
        self.genre_label.pack()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="🔀 Suggest another", command=self.suggest).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="✅ I'll watch this", command=self.mark_watched).grid(row=0, column=1, padx=5)

        rate_frame = tk.Frame(root)
        rate_frame.pack(pady=10)
        tk.Label(rate_frame, text="Rate after watching:").pack()
        stars = tk.Frame(rate_frame)
        stars.pack()
        for i in range(1, 6):
            tk.Button(stars, text=f"{i}⭐", command=lambda r=i: self.rate(r)).pack(side="left", padx=2)

        self.suggest()

    def suggest(self):
        recs = recommend(self.pool, top_n=5)
        if not recs:
            messagebox.showinfo("Done!", "You've rated everything in the pool — nice.")
            return
        self.current = recs[0]
        genres = [self.genre_map.get(g, "") for g in self.current.get("genre_ids", [])]
        self.title_label.config(text=f'{self.current["title"]}  ({self.current.get("release_date","")[:4]})')
        self.overview_label.config(text=self.current.get("overview", ""))
        self.genre_label.config(text=" • ".join(genres) + f'   |   TMDB: {self.current["vote_average"]}/10')

    def mark_watched(self):
        add_to_history(self.current["id"], self.current["title"], self.current.get("genre_ids", []))
        messagebox.showinfo("Logged", "Marked as watched. Rate it below once you're done!")

    def rate(self, stars):
        if not self.current:
            return
        add_to_history(self.current["id"], self.current["title"], self.current.get("genre_ids", []), user_rating=stars)
        messagebox.showinfo("Thanks!", f"Rated {stars}⭐ — I'll use this for future picks.")
        self.suggest()

if __name__ == "__main__":
    root = tk.Tk()
    app = MoviePickerApp(root)
    root.mainloop()