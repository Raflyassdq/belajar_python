import requests
import json

link = "http://universities.hipolabs.com/search?country=United+States"
respons = requests.get(link)
print (respons.json(), type(respons.json()))
