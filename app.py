import streamlit as st
from data_loader import load_data
from recommender import recommend_movies

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")

# Load dataset
movies, ratings = load_data()

# Select user ID
user_ids = ratings['userId'].unique()
user_id = st.selectbox("Select User ID", user_ids)

# Button to get recommendations
if st.button("Recommend Movies"):
    results = recommend_movies(user_id, movies, ratings)
    for _, row in results.iterrows():
        st.write("🎥", row['title'])
