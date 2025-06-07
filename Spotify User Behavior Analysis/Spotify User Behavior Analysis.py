# --------------------------------------------
# 🎵 Spotify User Behavior Analysis
# 📊 Exploratory Data Analysis (EDA) with Python
# Tools: Pandas, Matplotlib, Seaborn
# Author: [Your Name]
# --------------------------------------------

# 1. 📦 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: set style
sns.set(style="whitegrid")

# 2. 📁 Load Cleaned Dataset
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Ensure 'date' is a datetime object
df['date'] = pd.to_datetime(df['date'])

# --------------------------------------------
# 3. 🥇 Top 10 Most Streamed Songs Overall
# --------------------------------------------
top_songs = (
    df.groupby('track_name')['streams']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_songs, x='streams', y='track_name', palette='magma')
plt.title('Top 10 Most Streamed Songs')
plt.xlabel('Total Streams')
plt.ylabel('Song')
plt.tight_layout()
plt.savefig("images/top_10_songs.png")
plt.show()

# --------------------------------------------
# 4. 👨‍🎤 Top 10 Most Streamed Artists
# --------------------------------------------
top_artists = (
    df.groupby('artist')['streams']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_artists, x='streams', y='artist', palette='cool')
plt.title('Top 10 Most Streamed Artists')
plt.xlabel('Total Streams')
plt.ylabel('Artist')
plt.tight_layout()
plt.savefig("images/top_10_artists.png")
plt.show()

# --------------------------------------------
# 5. 📈 Daily Global Streams Over Time
# --------------------------------------------
daily_streams = (
    df.groupby('date')['streams']
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_streams, x='date', y='streams', color='blue')
plt.title('Daily Global Spotify Streams Over Time')
plt.xlabel('Date')
plt.ylabel('Total Streams')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/daily_streams_trend.png")
plt.show()

# --------------------------------------------
# 6. 🌍 Top 10 Streaming Regions (Countries)
# --------------------------------------------
region_streams = (
    df.groupby('region')['streams']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_regions = region_streams.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_regions, x='streams', y='region', palette='viridis')
plt.title('Top 10 Streaming Regions')
plt.xlabel('Total Streams')
plt.ylabel('Region')
plt.tight_layout()
plt.savefig("images/top_10_regions.png")
plt.show()

# --------------------------------------------
# 7. 🇺🇸 vs 🇬🇧 Top 5 Songs in US vs UK
# --------------------------------------------
us_uk_df = df[df['region'].isin(['us', 'gb'])]

top_songs_by_region = (
    us_uk_df.groupby(['region', 'track_name'])['streams']
    .sum()
    .reset_index()
)

top_us = top_songs_by_region[top_songs_by_region['region'] == 'us'].sort_values(by='streams', ascending=False).head(5)
top_uk = top_songs_by_region[top_songs_by_region['region'] == 'gb'].sort_values(by='streams', ascending=False).head(5)

top_combined = pd.concat([top_us, top_uk])
top_combined['label'] = top_combined['region'].map({'us': '🇺🇸 US', 'gb': '🇬🇧 UK'}) + " - " + top_combined['track_name']

plt.figure(figsize=(12, 6))
sns.barplot(data=top_combined, x='streams', y='label', hue='region', palette='Set2')
plt.title('Top 5 Most Streamed Songs: US vs UK')
plt.xlabel('Total Streams')
plt.ylabel('Song')
plt.tight_layout()
plt.savefig("images/us_vs_uk_songs.png")
plt.show()
