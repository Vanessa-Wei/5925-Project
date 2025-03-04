import requests
import os

# Set your API key
DEEPSEEK_API_KEY = "sk-2465de7ae65f4c6fb4d56e1d596b5006"

# DeepSeek API URL
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"


def generate_movie_review(movie_name):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",  # Specify the model
        "messages": [
            {"role": "system", "content": "You are a professional movie critic."},
            {"role": "user", "content": f"Write a detailed and engaging review for the movie '{movie_name}'. Include a summary, strengths, weaknesses, and final rating."}
        ],
        "temperature": 0.7
    }

    response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


# Example usage
movie_name = "Inception"
review = generate_movie_review(movie_name)
print("Generated Movie Review:")
print(review)