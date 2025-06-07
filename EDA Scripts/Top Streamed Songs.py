import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned dataset
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Optional: Set clean plot style
sns.set(style="whitegrid")

# Group by song + artist and sum total streams
top_songs = (
    df.groupby(['track_name', 'artist'])['streams']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# Create a combined label for plotting
top_songs['label'] = top_songs['track_name'] + " - " + top_songs['artist']

# Display in terminal
print("🎶 Top 10 Most Streamed Songs Overall:")
print(top_songs[['track_name', 'artist', 'streams']])

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x='streams', y='label', data=top_songs, palette='rocket')
plt.title('Top 10 Most Streamed Songs (Overall)', fontsize=14)
plt.xlabel('Total Streams')
plt.ylabel('Song - Artist')
plt.tight_layout()
plt.show()
