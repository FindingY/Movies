"""CSC 225: Movie Search starter project.

Complete the TODOs to create a movie search application using TMDB.
Do not put API credentials directly in this source file.
"""

import requests
import streamlit as st

SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w300"


def search_movies(title):
    """Search for a title and return a list of movie dictionaries.

    TODO:
      1. Read st.secrets["TMDB_READ_ACCESS_TOKEN"].
      2. Make a GET request to SEARCH_URL using requests.get(...).
         Use params={"query": title}, a Bearer authorization header,
         and timeout=10.
      3. Call response.raise_for_status().
      4. Convert the response to JSON and return its "results" list.
      5. Handle errors appropriately (in this function or the caller).
    """
    # Replace the placeholder below with your code.
    return []


def show_movie(movie):
    """Display one movie result.

    TODO:
      - Read values safely using dictionary .get(...).
      - Show the title, release year, TMDB rating, and overview.
      - If there is a poster_path, display POSTER_BASE_URL + poster_path.
      - Optional: use st.columns for a two-column layout.
    """
    st.write(movie.get("title", "Untitled movie"))
    # Add more result details here.


def main():
    st.title("Movie Search")
    st.caption("Search TMDB movie data using Python and Streamlit")

    title = st.text_input("Movie title", placeholder="e.g., The Matrix")
    if st.button("Search"):
        if not title.strip():
            st.warning("Please enter a movie title.")
            return

        # TODO: Call search_movies(title) and handle request errors.
        movies = search_movies(title.strip())
        if not movies:
            st.info("No results found (or search not implemented yet).")
            return

        # TODO: Iterate over at least five movies when available.
        for movie in movies[:10]:
            show_movie(movie)
            st.divider()


if __name__ == "__main__":
    main()
