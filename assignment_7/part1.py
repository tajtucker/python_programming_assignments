import pandas as pd

# Part 1
df = pd.read_csv('assignment_7/SampleAssignment7.csv')
print(df)

# Part 2
print(df.to_string(index=False))

# Part 3
print(df.head(3))

# Part 4
print(df.tail(3))

# Part 5
df.info()

# Part 6
print(df.shape)

# Part 7
my_df = df.dropna()
print(my_df)

# Part 8
my_df = df.dropna(subset=["Major"])
print(my_df)

# Part 9
my_df = df.dropna(axis=1)
print(my_df)

# Part 10
median_act = df["ACT"].median()
df["ACT"] = df["ACT"].fillna(median_act)
print(df)

# Part 11
df["Lastname"] = df["Lastname"].fillna("Rogers")
least_common_major = df["Major"].value_counts().idxmin()
df["Major"] = df["Major"].fillna(least_common_major)
print(df)

# Part 12
print(df.describe())
print(df["Classification"].describe())

# Part 13
df = df[~((df["Classification"] == "Senior") & (df["ACT"] < 30))]
print(df)

# Part 14
df = df.drop_duplicates()
print(df)

# Part 15
result = df[(df["Classification"] == "Senior") & (df["GPA"] < 3) & (df["ACT"] < 30)]
print(result)