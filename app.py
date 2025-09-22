import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("metadata.csv")
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

st.title("CORD-19 Data Explorer 🦠📊")
st.write("Explore COVID-19 research metadata interactively.")

# Sidebar filters
year_range = st.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (2020, 2021))

filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.write(f"Showing data for {len(filtered_df)} papers")

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Titles")
text = " ".join(filtered_df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.write(filtered_df.head())
