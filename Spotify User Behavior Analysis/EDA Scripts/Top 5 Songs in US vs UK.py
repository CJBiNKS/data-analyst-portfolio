import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Filter for US and UK regions
us_uk_df = df[df['region'].isin(['us', 'gb'])]  # 'gb' = United Kingdom country code

# Group by region and track name, sum the streams
top_songs = (
    us_uk_df.groupby(['region', 'track_name'])['streams']
    .sum()
    .reset_index()
)

# Get top 5 songs for each region
top_us = top_songs[top_songs['region'] == 'us'].sort_values(by='streams', ascending=False).head(5)
top_uk = top_songs[top_songs['region'] == 'gb'].sort_values(by='streams', ascending=False).head(5)

# Combine for plotting
top_combined = pd.concat([top_us, top_uk])

# Create a readable label for chart
top_combined['label'] = top_combined['region'].map({'us': '🇺🇸 US', 'gb': '🇬🇧 UK'}) + " - " + top_combined['track_name']

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=top_combined, y='label', x='streams', hue='region', palette='Set2')
plt.title('Top 5 Most Streamed Songs: US vs UK')
plt.xlabel('Total Streams')
plt.ylabel('Song')
plt.legend(title='Region', labels=['United Kingdom', 'United States'])
plt.tight_layout()
plt.show()
