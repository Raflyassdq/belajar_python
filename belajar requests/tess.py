import requests
import sqlite3

link = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
respons = requests.get(link)
#print (respons.json(), type(respons.json()))
data_json = respons.json()
data_us = data_json['data']

# Membuat atau membuka koneksi dengan database
conn = sqlite3.connect('imdb.db')
cursor = conn.cursor()

# Membuat tabel jika belum ada
create_table = ('''CREATE TABLE IF NOT EXISTS population (
                    ID_Nation TEXT,
                    Nation TEXT,
                    ID_Year INTEGER,
                    Year INTEGER,
                    Population INTEGER,
                    Slug_Nation TEXT
                )''')
cursor.execute(create_table)
conn.commit()

# Memasukkan data ke dalam tabel
for data in data_us:
    param = {}
    param['ID_Nation'] = data['ID Nation']
    param['Nation'] = data['Nation']
    param['ID_Year'] = data['ID Year']
    param['Year'] = data['Year']
    param['Population'] = data['Population']
    param['Slug_Nation'] = data['Slug Nation']
    # print('ID Nation:', data['ID Nation'])
    # print('Nation:', data['Nation'])
    # print('ID Year:', data ['ID Year'])
    # print('Year:', data ['Year'])
    # print('Population:', data['Population'])
    # print('Slug Nation:', data['Slug Nation'])
    print(param)
    
    cursor.execute('''INSERT INTO population (ID_Nation, Nation, ID_Year, Year, Population, Slug_Nation) VALUES (:ID_Nation, :Nation, :ID_Year, :Year, :Population, :Slug_Nation)''', param)
    conn.commit()
