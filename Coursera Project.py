import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv(
    r"/Users/adrianodicostanzo/Downloads/coursera dataset/CourseraDataset-Clean.csv"
)

# Renaming columns for conciseness
df.rename(
    columns={
        "Course Title": "title",
        "Rating": "rating",
        "Schedule": "schedule",
        "Offered By": "offered_by",
        "What you will learn": "objective",
        "Modules": "modules",
        "Course Url": "course_url",
        "Level": "level",
        "Skill gain": "skill",
        "Keyword": "keyword",
        "Instructor": "instructor",
        "Duration to complete (Approx.)": "duration",
        "Number of Review": "review_count",
    },
    inplace=True,
)

# Getting info about the DataFrame
df.info()

# Checking percentage of null values in DataFrame
print("% of Null Values")
missing_values = df.isnull().mean() * 100
print(round(missing_values, 2))

# Dropping null values
df.dropna(inplace=True)

# Checking for duplicates
print(df.duplicated().sum())

# No duplicates!

# Checking columns for correlation, building correlation matrix
from sklearn.preprocessing import LabelEncoder

encoded_df = df.copy()
encoder = LabelEncoder()
for column in encoded_df.columns:
    encoded_df[column] = encoder.fit_transform(encoded_df[column])

corr = encoded_df.corr()

fig = plt.figure(figsize=(8, 6))
sbn.heatmap(corr.round(2), annot=True)
plt.title("Correlation Matrix")
plt.tight_layout()

plt.show()

# No useful correlation between columns.

# Bar chart of course difficulty
pct_skill = df["level"].value_counts(normalize=True) * 100
print(pct_skill)

labels = df["level"].unique()

fig = plt.figure(figsize=(8, 6))
sbn.barplot(x=labels, y=pct_skill, palette="PuBuGn_r", hue=labels, legend=False)
sbn.color_palette("pastel")
plt.ylim(0, 100)
plt.title("Distribution of Skill Level")

plt.show()

# Majority of Coursera courses are geared towards beginners.

# Top 10 titles by rating and review count
subset_df = df[["title", "keyword", "rating", "review_count"]]

toptitles = (
    subset_df.sort_values(["rating", "review_count"], ascending=False)
    .head(10)
    .reset_index()
)
print("Top 10 Titles Across Categories")
print(toptitles)

# # Listing the most popular categories based on review count
cat_reviews = toptitles.set_index("keyword")
print()

# # Variables for analysis
keywords = df["keyword"].unique()
mean_kw_rating = df.groupby("keyword")["rating"].mean().round(2)
sorted_means = mean_kw_rating.sort_values(ascending=True)
# print(mean_kw_rating)

# # Sorting data by keyword
crsera_ind = df.set_index(["keyword"])
crsera_srt = crsera_ind.sort_values(["rating", "review_count"], ascending=False)

# Visualizing rating frequency

fig = plt.figure(figsize=(8, 6))
ax = sbn.barplot(
    x="keyword",
    y="rating",
    data=df,
    palette="PuBuGn_r",
    hue='keyword',
    legend=False,
)

ax.set_xticklabels(ax.get_xticklabels(), fontsize=8, rotation=40, ha="right")
ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)
plt.xlabel("Category")
plt.ylabel("Mean Rating")
plt.title("Mean Rating by Category")
plt.tight_layout()
plt.show()
