# Movie Search — Streamlit Starter Project

**Course:** CSC 225 — Data Structures  
**Language:** Python 3  
**Tools:** Streamlit, Requests, TMDB API

## Overview

Build a simple web application that allows a user to search for movies by title. Use **TMDB (The Movie Database)** for movie information, since IMDb does not offer a straightforward free public movie-search API. The finished application should display movie titles, release dates, ratings, descriptions, and available posters.

You will complete the starter code in `app.py` yourself. **Do not commit your API token.**

## 1. Setup

1. Create a [TMDB](https://www.themoviedb.org/) account and get a **Read Access Token** from your API settings.
2. Open this project in VS Code or another editor.
3. In the project directory, create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate            # macOS / Linux
   # Windows (PowerShell): .venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

5. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and replace the placeholder token with your own. The real secrets file is ignored by Git.
6. Start the app:

   ```bash
   python3 -m streamlit run app.py
   ```

7. Open the **Local URL** printed in the terminal (usually `http://localhost:8501`).

## 2. Build the interface

Your app should include a title, a text input, a search button, and a space for results. Look up `st.title`, `st.text_input`, `st.button`, `st.write`, `st.image`, and `st.columns` in the [Streamlit documentation](https://docs.streamlit.io/).

**Checkpoint:** Enter a title and click Search. Your interface runs even before connecting the API.

## 3. Query TMDB

Study the [TMDB Search Movie endpoint](https://developer.themoviedb.org/reference/search-movie). Use `requests.get` to send a request to:

```text
https://api.themoviedb.org/3/search/movie
```

Include the user-entered title in a `query` parameter and your token in the `Authorization: Bearer ...` header. Add a request timeout. Check for HTTP errors, then decode the response with `.json()`.

**Checkpoint:** Temporarily inspect the JSON response with `st.write()` or `print()`.

## 4. Process the response

Complete the `search_movies(title)` function in `app.py`. Return a **list of movie dictionaries** from the JSON `results` field. You should understand how to work with these fields:

| JSON key | Meaning |
| --- | --- |
| `title` | Movie title |
| `release_date` | Release date |
| `vote_average` | TMDB average user rating (not an IMDb rating) |
| `overview` | Plot description |
| `poster_path` | Relative poster image path |
| `id` | TMDB movie identifier |

**Checkpoint:** Searching for a movie title returns a list that you can iterate over.

## 5. Display results

For each result, display the title, release year, rating, short overview, and poster if available. Aim to display **at least five results** whenever the API returns enough matches. TMDB poster paths can be combined with the image base URL `https://image.tmdb.org/t/p/w300`.

Try placing poster and text in two `st.columns`.

## 6. Handle errors

Your application should not crash if:

- The input is empty or only spaces.
- The search returns no matches.
- The API fails or times out.
- A result has a missing poster, date, or overview.

Show clear user-facing messages for errors.

## 7. Optional enhancements

- Sort results by rating or release date.
- Filter by a user-selected minimum rating.
- Add links to movie detail pages.
- Allow users to save favorites in a list during a session.
- Add a title-based recommendation feature.

## Submission

Push your code to a **public GitHub repository** and submit the link. Include:

- `app.py` with your completed solution
- `requirements.txt`
- This `README.md` (you may add notes)
- A brief explanation of the Python lists and dictionaries used in your program

**Never push `.streamlit/secrets.toml` or your real token.**

## Completion checklist

- [ ] App launches successfully with Streamlit
- [ ] User can enter a title and search
- [ ] Live search results are retrieved from TMDB
- [ ] Results are processed using Python lists and dictionaries
- [ ] At least five matches appear when available
- [ ] Title, date, rating, description, and available poster are displayed
- [ ] Missing input, empty results, and API errors are handled
- [ ] Repository contains setup instructions and no secret tokens

## References

- [Streamlit documentation](https://docs.streamlit.io/)
- [TMDB API documentation](https://developer.themoviedb.org/docs/getting-started)
- [TMDB Search Movie endpoint](https://developer.themoviedb.org/reference/search-movie)

Movie data and images provided by TMDB. This project uses the TMDB API but is not endorsed or certified by TMDB.
