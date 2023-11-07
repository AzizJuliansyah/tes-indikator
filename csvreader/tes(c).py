import pandas as pd

data = pd.read_csv("movies1.csv")

data['Income'] = data['Income'].str.replace('$', '').str.replace(',', '')
data['Budget'] = data['Budget'].str.replace('$', '').str.replace(',', '').str.replace('SEK', '').str.replace(' ', '').str.replace('€', '').str.replace('₹', '').str.replace('DKK', '').str.replace('£', '').str.replace('₩', '').str.replace('¥', '').str.replace('A', '').str.replace('NOK', '').str.replace('C', '').str.replace('N', '')
data = data[data['Income'] != "Unknown"]
data = data[data['Budget'] != "Unknown"]
data['Income'] = data['Income'].astype(float)
data['Budget'] = data['Budget'].astype(float)
profitable_films = data[data['Income'] > data['Budget']]
print(profitable_films)

jumlah_film_keuntungan = profitable_films.shape[0]
print("Jumlah film yang mendapatkan keuntungan:", jumlah_film_keuntungan)