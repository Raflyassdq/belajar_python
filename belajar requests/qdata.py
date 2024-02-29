import requests
import json
import sqlite3

link = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
respons = requests.get(link)
#print (respons.json(), type(respons.json()))
data_json = respons.json()
data_us = data_json['data']

koneksi = sqlite3.connect('imdb.db')
cursor = koneksi.cursor()

buat_tabel = '''CREATE TABLE IF NOT EXISTS population (
                ID_Nation TEXT,
                Nation TEXT,
                ID_Year INTEGER,
                Year INTEGER,
                Population INTEGER,
                Slug_Nation TEXT);'''

cursor.execute(buat_tabel)
koneksi.commit()

for data in data_us:
   print(data)
         
cursor.executemany("INSERT INTO population VALUES (?,?,?,?,?,?);", )
koneksi.commit()


