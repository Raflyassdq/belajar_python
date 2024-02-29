import requests
import json
import sqlite3

link = "https://api.nationalize.io?name=nathaniel"
respons = requests.get(link)
#print(respons.json(), type(respons.json()) )
data_json = respons.json()
data_nat =data_json['country']

koneksi = sqlite3.connect('imdb.db')
cursor = koneksi.cursor()

create_tabel = ('''CREATE TABLE IF NOT EXISTS identitas(
                    country_id TEXT,
                    probability INTEGER)
                    ''')

cursor.execute(create_tabel)
koneksi.commit()

for country in data_nat:
    param = {}
    param['country_id'],  country['countryid']
    param['probability'], country['probability']
    print(param)
    # print("country id", country["country_id"] )
    # print("probability", country["probability"])
    # print()
cursor.execute('''INSERT INTO identitas (country_id, probability) VALUES (:country_id, :probability)''', param)




