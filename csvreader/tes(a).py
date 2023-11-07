import pandas as pd

data = pd.read_csv("movies1.csv")

grouped_data = data.groupby("Certificate")
count_per_certificate = grouped_data["Title"].count()
print(count_per_certificate)
