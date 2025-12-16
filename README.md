Movie Recommendation System

Welcome to the Movie Recommendation System, a complete project built using Python, Pandas, Scikit-learn, and Streamlit. This system provides personalized movie recommendations based on user ratings using collaborative filtering. The project is beginner-friendly, fully interactive, and demonstrates end-to-end machine learning workflow for recommendation engines.

Features:

Recommend movies for a specific user based on similar users' ratings

Interactive web interface using Streamlit

Easy-to-use and beginner-friendly

Uses the MovieLens Small Dataset (~100,000 ratings, 9,700 movies)

Project Structure:

movie_recommendation_system/
├── data/
│   ├── movies.csv        # Movie details (ID, title, genres)
│   └── ratings.csv       # User ratings (userId, movieId, rating, timestamp)
├── src/
│   ├── app.py            # Streamlit app to run the recommendation system
│   ├── data_loader.py    # Loads movies.csv and ratings.csv
│   └── recommender.py    # Recommendation logic using collaborative filtering
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies


Installation & Setup:

Clone the repository:

git clone <your-github-repo-link>
cd movie_recommendation_system


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Install dependencies: pip install -r requirements.txt

Place the dataset in data/ folder:

Download MovieLens Small dataset: MovieLens Small

Extract movies.csv and ratings.csv into the data/ folder

Running the Web App:

streamlit run src/app.py


The app will open in your default browser

Select a User ID from the dropdown

Click "Recommend Movies" to see personalized recommendations

How It Works:

Data Loading (data_loader.py): Loads movies and ratings CSV files using Pandas

Recommendation Logic (recommender.py): Creates a user-item matrix, computes user-user similarity using cosine similarity, and recommends top movies that similar users liked but the selected user hasn’t watched

Web Interface (app.py): Interactive UI using Streamlit for selecting user ID and getting recommendations

Example Output:

🎬 Movie Recommendation System
Select User ID: [1, 2, 3, ...]
[ Recommend Movies Button ]
Recommended Movies:
🎥 Toy Story (1995)
🎥 Jumanji (1995)
🎥 Grumpier Old Men (1995)


Dataset Details:

movies.csv → Columns: movieId, title, genres

ratings.csv → Columns: userId, movieId, rating, timestamp

Dependencies:

Python 3.9+

pandas

scikit-learn

streamlit

Install all dependencies using: pip install -r requirements.txt

How to Contribute:

Fork the repository

Create a new branch (git checkout -b feature-name)

Make changes

Commit (git commit -m "Description")

Push (git push origin feature-name)

Open a Pull Request
