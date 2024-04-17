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
df2.dropna(inplace=True)
print(df2.info())

# Writing to .csv file

df2.to_csv("Reactions_Cleaned.csv")



# Cleaning Content dataset

print(df3.head())
print(df3.info())

# Dropping unneccessary "URL" column

df3.drop(["URL"], axis=1, inplace=True)
# print(df3.info())

# Renaming column "Type" to "Content Type" for specificity

df3.rename(columns={"Type": "Content Type"}, inplace=True)

# Stripping quotation marks "Category" values and standardizing capitalization
df3["Category"] = df3["Category"].str.strip('""')
df3["Category"] = df3["Category"].str.lower()
print(df3.iloc[:, 3].unique())


# Dropping null values, duplicates
df3.dropna(inplace=True)
df3.drop_duplicates(inplace=True)
print(df3.info())

# Writing to .csv file

df3.to_csv("Content_Cleaned.csv")
