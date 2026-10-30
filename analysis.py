import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

df = pd.read_csv("dataset/spotify-tracks-dataset-detailed.csv")

# Check dataset dimensions
print("Dataset Shape:")
print(df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns)

# Check dataset information
print("\nDataset Information:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())



# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check duplicate track IDs
print("\nDuplicate Track IDs:")
print(df["track_id"].duplicated().sum())


# Find records with duplicate track IDs
duplicate_tracks = df[df.duplicated(subset="track_id", keep=False)]

# Display the first 10 records
print("\nDuplicate Track Examples:")
print(duplicate_tracks[["track_id", "track_name", "artists", "track_genre"]].head(10))


# Get one duplicated track ID
duplicate_id = df[df.duplicated(subset="track_id", keep=False)]["track_id"].iloc[0]

# Display all records with that ID
print("\nSame Track ID Details:")
print(df[df["track_id"] == duplicate_id][
    ["track_id", "track_name", "artists", "track_genre"]
])


# Remove exact duplicate rows
df = df.drop_duplicates()

print("Dataset shape after removing duplicates:")
print(df.shape)


# Check missing values
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

print("\nDataset shape after cleaning:")
print(df.shape)

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum().sum())



# Basic statistical summary
print("\nStatistical Summary:")
print(df.describe())



# Convert duration from milliseconds to minutes
df["duration_min"] = df["duration_ms"] / 60000

print("\nTrack Duration in Minutes:")
print(df["duration_min"].describe())



# Find tracks longer than 15 minutes
long_tracks = df[df["duration_min"] > 15]

print("\nTracks Longer Than 15 Minutes:")
print(long_tracks[
    ["track_name", "artists", "duration_min", "track_genre"]
].sort_values(by="duration_min", ascending=False).head(10))

print("\nTotal Long Tracks:")
print(len(long_tracks))



# Check tracks with zero tempo
zero_tempo = df[df["tempo"] == 0]

print("\nTracks with Zero Tempo:")
print(len(zero_tempo))

print("\nExamples:")
print(zero_tempo[
    ["track_name", "artists", "tempo", "track_genre"]
].head(10))



# Check zero values in audio features

features = [
    "danceability",
    "energy",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

print("\nZero Values in Audio Features:")

for column in features:
    zero_count = (df[column] == 0).sum()
    print(column, ":", zero_count)



# Check tracks with zero tempo, danceability and speechiness

zero_tracks = df[
    (df["tempo"] == 0) &
    (df["danceability"] == 0) &
    (df["speechiness"] == 0)
]

print("Tracks with all three features equal to zero:")
print(len(zero_tracks))

print("\nExamples:")
print(zero_tracks[
    ["track_name", "artists", "track_genre"]
].head(10))


# Distribution of Track Popularity

plt.figure(figsize=(10, 5))

sns.histplot(df["popularity"], bins=20, kde=True)

plt.title("Distribution of Track Popularity")
plt.xlabel("Popularity")
plt.ylabel("Number of Tracks")

plt.show()

print("\nPopularity Statistics:")
print(df["popularity"].describe())

print("\nPopularity Distribution:")
print(df["popularity"].value_counts(bins=10).sort_index())

print("\nPopularity Statistics:")
print(df["popularity"].describe())


# Distribution of Track Popularity

plt.figure(figsize=(10, 5))

sns.histplot(df["popularity"], bins=20, kde=True)

plt.title("Distribution of Track Popularity")
plt.xlabel("Popularity")
plt.ylabel("Number of Tracks")

plt.savefig("visualizations/popularity_distribution.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Average Popularity by Genre

genre_popularity = df.groupby("track_genre")["popularity"].mean()

top_genres = genre_popularity.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))

sns.barplot(x=top_genres.values, y=top_genres.index)

plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Music Genre")

plt.savefig("visualizations/top_genres_popularity.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Average Popularity by Genre

genre_popularity = df.groupby("track_genre")["popularity"].mean()

top_genres = genre_popularity.sort_values(ascending=False).head(10)

print("\nTop 10 Genres by Average Popularity:")
print(top_genres)



print("GENRE CODE IS RUNNING")


# Top 10 Genres by Average Popularity

plt.figure(figsize=(12, 6))

sns.barplot(x=top_genres.values, y=top_genres.index)

plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Music Genre")

plt.savefig("visualizations/top_genres_popularity.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Top 10 Genres by Average Popularity

plt.figure(figsize=(12, 6))

sns.barplot(x=top_genres.values, y=top_genres.index)

plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Music Genre")

plt.savefig("visualizations/top_genres_popularity.png",
            dpi=300, bbox_inches="tight")

plt.show()

# Danceability vs Energy

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="danceability",
    y="energy",
    alpha=0.3
)

plt.title("Danceability vs Energy")
plt.xlabel("Danceability")
plt.ylabel("Energy")

plt.savefig("visualizations/danceability_vs_energy.png",
            dpi=300, bbox_inches="tight")

plt.show()

# Correlation Heatmap

audio_features = [
    "popularity",
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

correlation = df[audio_features].corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Spotify Audio Features")

plt.savefig("visualizations/correlation_heatmap.png",
            dpi=300, bbox_inches="tight")

plt.show()


# Strongest Correlations

correlation = df[audio_features].corr()

correlation_pairs = correlation.unstack()

correlation_pairs = correlation_pairs[
    correlation_pairs.index.get_level_values(0) !=
    correlation_pairs.index.get_level_values(1)
]

print("\nStrongest Correlations:")
print(correlation_pairs.sort_values(ascending=False).head(10))


# Explicit vs Non-Explicit Tracks

explicit_popularity = df.groupby("explicit")["popularity"].mean()

print("\nAverage Popularity by Explicit Status:")
print(explicit_popularity)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=explicit_popularity.index,
    y=explicit_popularity.values
)

plt.title("Average Popularity: Explicit vs Non-Explicit Tracks")
plt.xlabel("Explicit Content")
plt.ylabel("Average Popularity")

plt.savefig("visualizations/explicit_vs_non_explicit.png",
            dpi=300, bbox_inches="tight")

plt.show()

# Strongest Correlations

correlation = df[audio_features].corr()

correlation_pairs = correlation.unstack()

correlation_pairs = correlation_pairs[
    correlation_pairs.index.get_level_values(0) !=
    correlation_pairs.index.get_level_values(1)
]

print("\nStrongest Correlations:")
print(correlation_pairs.sort_values(ascending=False).head(10))


# Correlation with Popularity

print("\nCorrelation with Popularity:")
print(correlation["popularity"].sort_values(ascending=False))