import requests

url = "https://www.kucoin.com/_api/cms/articles?page=1&pageSize=10&category=listing&lang=en_US"

res = requests.get(url)
list = res.json()
print("---------------------------------")
print(list)
print("---------------------------------")