import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Group by region (country code) and sum streams
region_streams = (
    df.groupby('region')['streams']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# Get top 10 regions
top_regions = region_streams.head(10)

# Print to terminal
print("🌍 Top 10 Streaming Regions:")
print(top_regions)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='streams', y='region', data=top_regions, palette='coolwarm')
plt.title('Top 10 Streaming Regions by Total Spotify Streams')
plt.xlabel('Total Streams')
plt.ylabel('Region (Country Code)')
plt.tight_layout()
plt.show()
