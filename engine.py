import pandas as pd

metadata = pd.read_csv("movies_metadata.csv", low_memory=False)

# print(metadata.head())

C = metadata["vote_average"].mean()
print(f"Vote average mean: {C}")
# this returns 5.618...
# Shows how all movies from this dataset have that average rating of 1-10

# Calculates the min number of votes required to be in the chart
M = metadata["vote_count"].quantile(0.9)
print(f"Vote count quantile: {M}")
# this returns 160.0

# Use the copy() method to ensure a new pandas DataFrame can be independantly created
# based off the original DataFrame
q_movies = metadata.copy()["vote_count"]
print(q_movies.shape)
# use a logical operator to filter movies greater than or equal to 160 vote counts
