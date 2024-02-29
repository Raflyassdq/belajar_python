import sqlite3
import requests
# Membuat atau membuka koneksi dengan database
conn = sqlite3.connect('imdb.db')
cursor = conn.cursor()

link = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
respons = requests.get(link)
#print (respons.json(), type(respons.json()))
data_json = respons.json()
data_us = data_json['data']

# Membuat tabel jika belum ada
cursor.execute('''CREATE TABLE IF NOT EXISTS population (
                    ID_Nation TEXT,
                    Nation TEXT,
                    ID_Year INTEGER,
                    Year INTEGER,
                    population INTEGER,
                    Slug_Nation TEXT
                )''')

# Memasukkan data ke dalam tabel
for data in data_us:
    print(data)
    
    cursor.execute('''INSERT INTO population VALUES (?, ?, ?, ?, ?, ?)''', )
