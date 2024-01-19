from config import API_KEY
import requests
import json

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&outputsize=full&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

with open('data/stock-data.json', 'w') as out_file:
    json.dump(data, out_file)
