import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("\nCleaned dataset preview:")
print(df.head())
print("\nFinal dataset shape:", df.shape)

df.to_csv("spotify_streaming_cleaned.csv", index=False)
print("\n✅ Cleaned data saved as 'spotify_streaming_cleaned.csv'")

