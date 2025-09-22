# Handle missing values
missing_threshold = 0.5  # drop cols with >50% missing
df = df.dropna(axis=1, thresh=len(df)*missing_threshold)

# Drop rows missing critical info (title, publish_time)
df = df.dropna(subset=["title", "publish_time"])

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Add abstract word count
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))
