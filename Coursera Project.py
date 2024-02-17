import pandas as pd
import matplotlib.pyplot as plt

coursera_df = pd.read_csv(
    r"/Users/adrianodicostanzo/Downloads/coursera dataset/CourseraDataset-Clean.csv"
)

# Renaming columns for conciseness
coursera_df.rename(
    columns={
        "Course Title": "title",
        "Rating": "rating",
        "Level": "level",
        "Skill gain": "skill",
        "Keyword": "keyword",
        "Instructor": "instructor",
        "Duration to complete (Approx.)": "duration",
        "Number of Review": "review_count",
    },
    inplace=True,
)

# Top 10 titles by rating and review count
crsera_subset = coursera_df[["title", "keyword", "rating", "review_count"]]

toptitles = (
    crsera_subset.sort_values(["rating", "review_count"], ascending=False)
    .reset_index()
    .iloc[:10]
)
print(toptitles)

# Listing the most popular categories based on review count
cat_reviews = toptitles.set_index("keyword")
print()

# Variables for analysis
keywords = pd.unique(coursera_df["keyword"])
mean_kw_duration = coursera_df.groupby("keyword")["rating"].mean()

# Sorting data by keyword
crsera_ind = coursera_df.set_index(["keyword"])

crsera_srt = crsera_ind.sort_values(["rating", "review_count"], ascending=False)

# Visualizing rating frequency

# plt.bar(keywords, mean_kw_duration, color="purple", edgecolor="black")
# plt.xlabel("Category")
# plt.ylabel("Mean Duration (hr)")
# plt.title("Mean Duration by Category")

# plt.show()
