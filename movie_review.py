import openai
import os
from dotenv import load_dotenv
import random

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("ERROR: API Key not found! Make sure it's set in your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

def extract_movie_name_from_srt(file_path):
    """
    Function to extract the movie name from an SRT file.
    This assumes the movie name is in the SRT file's filename.
    Args:
        file_path (str): The path to the SRT file
    Returns:
        str: The extracted movie name
    """
    # Extract the movie name from the SRT file's name (without the extension)
    movie_name = os.path.basename(file_path).replace('.srt', '')
    return movie_name


def get_movie_review(movie_name):
    """Generates a movie review for the given movie name using OpenAI API."""
    prompt = f"Write a detailed and engaging review for the movie '{movie_name}'. Include a summary, strengths, weaknesses, and final rating."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content

# # Path to the SRT file
# srt_file_path = "/Users/lai/IdeaProjects/Project 5925/Subtitlesforoscarandblockbusters/Blockbusters/1950/Broken Arrow.srt"
#
# # Extract the movie name from the SRT file
# movie_name = extract_movie_name_from_srt(srt_file_path)
#
# # Generate the movie review using the movie name
# movie_review = get_movie_review(movie_name)
#
# # Print the generated movie review
# print("Generated Movie Review:")
# print(movie_review)

def generate_reviews_for_selected_movies(movie_files):
    """Generates movie reviews for a list of selected movie files."""
    reviews = {}
    for movie_file in movie_files:
        movie_name = extract_movie_name_from_srt(movie_file)
        review = get_movie_review(movie_name)
        reviews[movie_name] = review
    return reviews

# Specify the root directory where the movie SRT files are stored
root_directory = "/Users/lai/IdeaProjects/Project 5925/Subtitlesforoscarandblockbusters/Blockbusters"

# Function to get all SRT files from the directory
def get_all_srt_files(directory):
    srt_files = []
    for year in range(1950, 2025):  # Adjust the years range as needed
        year_directory = os.path.join(directory, str(year))
        if os.path.isdir(year_directory):
            for file_name in os.listdir(year_directory):
                if file_name.endswith(".srt"):
                    srt_files.append(os.path.join(year_directory, file_name))
    return srt_files

# Get all SRT files from the Blockbusters folder
all_srt_files = get_all_srt_files(root_directory)

# Randomly select 20 movies
random_selected_files = random.sample(all_srt_files, 20)

# Generate reviews for the selected 20 movies
movie_reviews = generate_reviews_for_selected_movies(random_selected_files)

# Print the generated movie reviews
for movie_name, review in movie_reviews.items():
    print(f"Review for {movie_name}:")
    print(review)
    print("\n" + "-"*50 + "\n")