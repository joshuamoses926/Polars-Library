import polars as pl
df = pl.read_csv('iris.csv')

#print the first 5 rows of the csv
print(df.head())

#print general summary statistics using describe()
print(df.describe())

#Filter the dataset for specific species (i.e., "Setosa")
filtered_df = df.filter(pl.col("species") == "setosa")
print(filtered_df)