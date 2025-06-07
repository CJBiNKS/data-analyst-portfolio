import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned dataset
df = pd.read_csv("spotify_streaming_cleaned.csv")

# Make sure the date column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum streams
daily_streams = df.groupby('date')['streams'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_streams, x='date', y='streams', color='blue')
plt.title('📈 Daily Global Spotify Streams Over Time', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Total Streams')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
