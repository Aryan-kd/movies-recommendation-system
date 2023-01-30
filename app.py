import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pd.DataFrame(movies)


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=a84789552d9d24778f934dadee383c61'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_listed = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_poster = []
    for j in movies_listed:
        movie_id = movies_list.iloc[j[0]].movie_id
        recommended_movies.append(movies_list.iloc[j[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Which movie you would like to watch",
    movies_list['title'].values)

if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col1:
        st.text(names[3])
        st.image(poster[3])
    with col2:
        st.text(names[4])
        st.image(poster[4])
    with col3:
        st.text(names[5])
        st.image(poster[5])
    with col1:
        st.text(names[6])
        st.image(poster[6])
    with col2:
        st.text(names[7])
        st.image(poster[7])
    with col3:
        st.text(names[8])
        st.image(poster[8])
    with col1:
        st.text(names[9])
        st.image(poster[9])
