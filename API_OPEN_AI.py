# uses OpenAI's GPT API to generate a movie review for a given movie title.

import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("ERROR: API Key not found! Make sure it's set in your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

def get_movie_review(movie_name):
    """Generates a movie review for the given movie name using OpenAI API."""
    prompt = f"Write a detailed and engaging review for the movie '{movie_name}'. Include a summary, strengths, weaknesses, and final rating."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content

# Get user input for movie name
movie_name = input("Enter the movie name: ")
review = get_movie_review(movie_name)

# Print the review
print("\nMovie Review:\n")
print(review)
