import pandas as pd

def load_data():
    # Load movies and ratings CSV files
    movies = pd.read_csv('data/movies.csv')
    ratings = pd.read_csv('data/ratings.csv')
    return movies, ratings

