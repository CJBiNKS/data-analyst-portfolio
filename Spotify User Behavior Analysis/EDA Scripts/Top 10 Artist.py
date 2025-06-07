import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Optional style
sns.set(style="whitegrid")

# Group and sort
top_artists = df.groupby('artist')['streams'].sum().sort_values(ascending=False).head(10)

# Print results
print("🎵 Top 10 Artists by Total Streams:")
print(top_artists)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_artists.values, y=top_artists.index, palette="mako")
plt.title("Top 10 Most Streamed Artists (Overall)", fontsize=14)
plt.xlabel("Total Streams")
plt.ylabel("Artist")
plt.tight_layout()
plt.show()
