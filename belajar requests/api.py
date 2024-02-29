import requests
import json

link = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
respons = requests.get(link)
#print (respons.json(), type(respons.json()))
data_json = respons.json()
data_us = data_json['data']

for data in data_us:
    print(data)