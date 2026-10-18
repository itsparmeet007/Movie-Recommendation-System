import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie data
@st.cache_data
def load_movies():
    with open("movies_dict.pkl", "rb") as file:
        movies_dict = pickle.load(file)

    return pd.DataFrame(movies_dict)

movies = load_movies()

# Convert movie tags into vectors once
@st.cache_resource
def load_vectors():
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(movies["tag"].fillna(""))
    return vectors

vectors = load_vectors()
# TMDB API key
API_KEY = st.secrets["TMDB_API_KEY"]

# Fetch movie poster using TMDB API
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    for attempt in range(3):
        try:
            response = requests.get(
                url,
                params={
                    "api_key": API_KEY,
                    "language": "en-US"
                },
                timeout=15
            )

            if response.status_code == 200:
                data = response.json()
                poster_path = data.get("poster_path")

                if poster_path:
                    return (
                        "https://image.tmdb.org/t/p/w500"
                        + poster_path
                    )

                return None

            # Retry temporary server or rate-limit errors
            if response.status_code not in (429, 500, 502, 503, 504):
                return None

        except requests.RequestException:
            if attempt == 2:
                return None

    return None


# Recommend similar movies
def recommend(movie):
    matches = movies.index[movies["title"] == movie]

    if len(matches) == 0:
        return [], []

    movie_index = matches[0]

    # Calculate similarity only for the selected movie
    similarity_scores = cosine_similarity(
        vectors[movie_index],
        vectors
    ).flatten()

    # Sort by highest similarity and exclude the selected movie
    movie_list = sorted(
        enumerate(similarity_scores),
        key=lambda x: x[1],
        reverse=True
    )

    movie_list = [
        (idx, score)
        for idx, score in movie_list
        if idx != movie_index
    ][:5]

    recommended_movie_names = []
    recommended_movie_posters = []

    for idx, score in movie_list:
        movie_data = movies.iloc[idx]

        recommended_movie_names.append(movie_data["title"])
        recommended_movie_posters.append(
            fetch_poster(movie_data["movie_id"])
        )

    return recommended_movie_names, recommended_movie_posters


# Streamlit interface
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Which movie would you like to recommend?",
    movies["title"].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    if names:
        st.subheader("Recommended Movies")

        cols = st.columns(5)

        for i, col in enumerate(cols):
            with col:
                st.write(names[i])

                if posters[i]:
                    st.image(
                        posters[i],
                        use_container_width=True
                    )
                else:
                    st.caption("Poster unavailable")
    else:
        st.warning("No recommendations found.")
