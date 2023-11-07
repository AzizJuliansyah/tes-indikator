import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv("movies1.csv")

# Konversi kolom "Rating" ke tipe data float
data['Rating'] = data['Rating'].astype(float)

# Mengelompokkan data berdasarkan kolom "Month" (bulan) dan mengambil 5 film dengan rating tertinggi dalam setiap bulan
top_5_per_month = data.groupby('Month').apply(lambda x: x.nlargest(5, 'Rating')).reset_index(drop=True)

# Mengurutkan hasil berdasarkan bulan dan rating (secara default, mengurutkan dari terendah ke tertinggi)
top_5_per_month = top_5_per_month.sort_values(['Month', 'Rating'])

# Menampilkan 5 film teratas untuk setiap bulan
print(top_5_per_month)
