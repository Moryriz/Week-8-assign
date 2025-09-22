import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Count papers by year
year_counts = df["year"].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# 2. Top publishing journals
top_journals = df["journal"].value_counts().head(10)
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.show()

# 3. Word cloud of titles
text = " ".join(df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# 4. Distribution by source
sns.countplot(y="source_x", data=df, order=df["source_x"].value_counts().index[:10])
plt.title("Paper Counts by Source")
plt.show()
