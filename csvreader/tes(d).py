import pandas as pd

data = pd.read_csv("movies1.csv")
bulan_terbanyak = data['Month'].value_counts().idxmax()
print("Bulan dengan jumlah film terbanyak:", bulan_terbanyak)
