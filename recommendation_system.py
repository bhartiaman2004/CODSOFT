# List of movies with genres and directors
movies = [
    {"title": "The Matrix", "genre": "Action", "director": "Lana Wachowski"},
    {"title": "Inception", "genre": "Action", "director": "Christopher Nolan"},
    {"title": "The Lion King", "genre": "Animation", "director": "Roger Allers"},
    {"title": "Interstellar", "genre": "Sci-Fi", "director": "Christopher Nolan"},
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "Finding Nemo", "genre": "Animation", "director": "Andrew Stanton"},
    {"title": "Pulp Fiction", "genre": "Crime", "director": "Quentin Tarantino"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"}
]

# Function to find a movie by title
def find_movie_by_title(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():  # Ignore case
            return movie
    return None

# Get a list of movies the user likes (input from the user)
user_likes = []
print("Enter the movies you like (type 'done' when finished):")
while True:
    user_input = input("Movie title: ")  # Take input from the user
    if user_input.lower() == 'done':  # Stop when the user types 'done'
        break
    movie = find_movie_by_title(user_input)  # Check if the movie exists in the list
    if movie:
        user_likes.append(movie)  # Add to user likes
    else:
        print("Movie not found in the list. Please try again.")

# Function to recommend movies based on user preferences
def recommend_movies(user_likes, movies):
    recommendations = []
    for movie in movies:
        for liked_movie in user_likes:
            if movie["genre"] == liked_movie["genre"] or movie["director"] == liked_movie["director"]:
                if movie not in user_likes and movie not in recommendations:
                    recommendations.append(movie)
    return recommendations

# Get recommendations and print them
recommendations = recommend_movies(user_likes, movies)
print("\nRecommended Movies:")
for movie in recommendations:
    print(f"- {movie['title']}")