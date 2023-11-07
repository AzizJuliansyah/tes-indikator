import pandas as pd

data = pd.read_csv("movies1.csv")

high_rating_films = data[data['Rating'] > 7.5]
director_counts = high_rating_films['Directors'].value_counts()
prolific_directors = director_counts[director_counts > 1]
print(prolific_directors)
