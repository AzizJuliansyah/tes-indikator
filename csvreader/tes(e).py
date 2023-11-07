import pandas as pd

data = pd.read_csv("movies1.csv")
data['Rating'] = data['Rating'].astype(float)

top_5_per_month = data.groupby('Month').apply(lambda x: x.nlargest(5, 'Rating')).reset_index(drop=True)

top_5_per_month = top_5_per_month.sort_values(['Month', 'Rating'])

print(top_5_per_month)
