import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def create_user_item_matrix(ratings):
    # Create a user-item rating matrix
    return ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

def recommend_movies(user_id, movies, ratings, top_n=5):
    # Create user-item matrix
    matrix = create_user_item_matrix(ratings)
    
    # Compute cosine similarity between users
    similarity = cosine_similarity(matrix)
    sim_df = pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)
    
    # Find most similar users
    similar_users = sim_df[user_id].sort_values(ascending=False)[1:6]
    
    # Movies already rated by the user
    user_movies = ratings[ratings.userId == user_id].movieId
    
    # Get recommended movies from similar users
    recommendations = ratings[ratings.userId.isin(similar_users.index) & ~ratings.movieId.isin(user_movies)]
    top_movies = recommendations.groupby('movieId').mean().sort_values('rating', ascending=False).head(top_n)
    
    # Return recommended movie titles
    return movies[movies.movieId.isin(top_movies.index)]
