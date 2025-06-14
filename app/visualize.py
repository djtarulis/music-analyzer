import json
import matplotlib.pyplot as plt
from collections import Counter

# Load music data from JSON file
with open("music_data.json", "r") as f:
    music_data = json.load(f)

# Extract data
tempos = [info["tempo"] for info in music_data.values() if info["tempo"] is not None]
genres = [info["genre"] for info in music_data.values() if info["genre"]]
pitches = [info["pitch"] for info in music_data.values() if info["pitch"]]

genre_counts = Counter(genres)
pitch_counts = Counter(pitches)

# Prepare genre labels and values (top 6 + Other)
top_genres = genre_counts.most_common(6)
labels, values = zip(*top_genres)
other_count = sum(genre_counts.values()) - sum(values)
labels += ("Other",)
values += (other_count,)

# Create a dashboard layout with 1 row and 3 columns
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Tempo histogram
axs[0].hist(tempos, bins=10, edgecolor='black')
axs[0].set_title("Tempo Distribution")
axs[0].set_xlabel("Tempo (BPM)")
axs[0].set_ylabel("Number of Songs")
axs[0].grid(True)

# Plot 2: Genre pie chart
axs[1].pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
axs[1].set_title("Genre Distribution")
axs[1].axis('equal')  # Equal aspect ratio makes pie circular

# Plot 3: Pitch bar chart
axs[2].bar(pitch_counts.keys(), pitch_counts.values(), color='skyblue', edgecolor='black')
axs[2].set_title("Most Common Dominant Pitches")
axs[2].set_xlabel("Pitch")
axs[2].set_ylabel("Number of Songs")
axs[2].grid(axis='y')

plt.tight_layout()
plt.show()