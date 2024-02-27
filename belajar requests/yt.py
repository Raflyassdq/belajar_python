#https://api.namefake.com/indonesian-indonesia/random
#https://api.akuari.my.id/downloader/tiktok?link=https://vm.tiktok.com/ZSJcLPNpe
#https://httpbin.org

import requests

link = "https://httpbin.org"
respons = requests.get(link)
print(respons.text)
