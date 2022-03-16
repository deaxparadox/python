import pandas as pd

df = pd.DataFrame(
{
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnel, Miss. Elizabeth",
    ],
    "Age":[22,35,58],
    "Sex": ["male", "make", "female"]
})
print(df)

# A DataFrame is a 2-dimensional data structure that can store
# data of different types (including characters, integers, floating
# point values, categorical data and more) in columns

# Each column is a DataFrame is a Series

print(df["Age"])

# Creating a series from scratch 
ages = pd.Series([22,35,58], name="age")
print(ages)
# a pandas series has no column labels, as it is just a single 
# column of a DataFrame.

# max() value in series
print(df['Age'].max())

# describe() method provides a quick overview of the numerical data in 
# a DataFrame. As the Name and Sex columns are textual data, these are by default not taken 
# into account by the describe() method.
print(df.describe())