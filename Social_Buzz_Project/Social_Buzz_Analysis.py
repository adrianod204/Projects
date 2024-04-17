import pandas as pd

# Loading tables as Pandas DataFrames

df1 = pd.read_csv(
    r"/Users/adrianodicostanzo/Downloads/ReactionTypes.csv", index_col=[0]
)
df2 = pd.read_csv(r"/Users/adrianodicostanzo/Downloads/Reactions.csv", index_col=[0])
df3 = pd.read_csv(r"/Users/adrianodicostanzo/Downloads/Content.csv", index_col=[0])

# Cleaning Reaction Types dataset

df1.drop_duplicates(inplace=True)
df1.dropna(inplace=True)

# Writing to .csv file

df1.to_csv("ReactionTypes_Cleaned.csv")


# Cleaning Reactions dataset

df2.drop_duplicates(inplace=True)
# df2.dropna(inplace=True)
print(df2.info())

# Dropping unnecessary "User ID" column
df2.drop(["User ID"], axis=1, inplace=True)

# Writing to .csv file

df2.to_csv("Reactions_Cleaned.csv")


# Cleaning Content dataset

print(df3.head())
print(df3.info())

# Dropping unnecessary "URL" and "User ID" columns

df3.drop(["URL"], axis=1, inplace=True)
df3.drop(["User ID"], axis=1, inplace=True)
# print(df3.info())

# Renaming column "Type" to "Content Type" for specificity

df3.rename(columns={"Type": "Content Type"}, inplace=True)

# Stripping quotation marks "Category" values and standardizing capitalization
df3["Category"] = df3["Category"].str.strip('""')
df3["Category"] = df3["Category"].str.lower()
# print(df3.iloc[:, 3].unique())


# Dropping null values, duplicates
df3.dropna(inplace=True)
df3.drop_duplicates(inplace=True)
print(df3.info())

# Writing to .csv file

df3.to_csv("Content_Cleaned.csv")

# Merging tables
reactionsdf = df2
contentdf = df3
rtypesdf = df1

merged_df = reactionsdf.merge(contentdf, on="Content ID", how="inner")

print(merged_df)

joined_df = rtypesdf.merge(merged_df, on="Type", how="inner")

print(joined_df)

# Grouping by Category to find the top 5 scoring categories

top5cats = (
    joined_df.groupby("Category")["Score"].sum().sort_values(ascending=False).head(5)
)

print(top5cats)

# Writing data to Excel spreadsheets

top5cats.to_excel("Top Five Categories.xlsx")
joined_df.to_excel("Cleaned Dataset.xlsx")
