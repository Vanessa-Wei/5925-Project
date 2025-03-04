import kagglehub
import os
import random

# kagglehub.login()

# # Download latest version
# path = kagglehub.dataset_download("mlopssss/subtitles")
#
# print("Path to dataset files:", path)

# Blockbuster movies from 1950 to 2024
# Oscar movies from 1950 to 2024

# Randomly select 20 movies from Oscar dataset
# Path to teh Oscar dataset
oscar_path = "/Users/lai/IdeaProjects/Project 5925/Subtitlesforoscarandblockbusters/Oscar"

# Set a specific random seed for reproducibility
random.seed(42)

# Ensure the directory exists
if not os.path.exists(oscar_path):
    raise FileNotFoundError(f"Path not found: {oscar_path}")

# Get all year folders (1950 to 2024)
year_folders = [os.path.join(oscar_path, folder) for folder in os.listdir(oscar_path) if folder.isdigit()]

# print(year_folders)

# Check if the dataset contains valid folders
if not year_folders:
    raise ValueError("No valid year folders found in the dataset path.")

# Store selected movie files
selected_movies_oscar = []

while len(selected_movies_oscar) < 20:
    year_folder = random.choice(year_folders)  # Randomly pick a year
    srt_files = [f for f in os.listdir(year_folder) if f.endswith(".srt")]

    if srt_files:  # Ensure there are subtitles in the folder
        selected_movie = random.choice(srt_files)
        selected_movies_oscar.append(os.path.join(year_folder, selected_movie))

# Print selected movies
print("Selected movies for research:")
for movie in selected_movies_oscar:
    print(movie)


# Explore the genres of Oscar-winning and Blockbuster movies from the text file
import re
from collections import Counter
# Path to the text file
file_path = "/Users/lai/IdeaProjects/Project 5925/titles with awards and categories.txt"

# Dictionaries to store genre counts
oscar_genres = Counter()
blockbuster_genres = Counter()

# Read and process the file
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        match = re.match(r"(.+?) \((\d{4}), (Oscar|Blockbusters)\), (.+)", line.strip())
        if match:
            movie, year, category, genre = match.groups()
            if category == "Oscar":
                oscar_genres[genre] += 1
            else:
                blockbuster_genres[genre] += 1

# Print top genres
print("Top Oscar-winning genres:")
for genre, count in oscar_genres.most_common(10):
    print(f"{genre}: {count}")

print("\nTop Blockbuster genres:")
for genre, count in blockbuster_genres.most_common(10):
    print(f"{genre}: {count}")