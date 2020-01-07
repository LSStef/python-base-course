import requests
import json

url = 'http://www.cbr-xml-daily.ru/daily_jsonp.js'
response = requests.get(url)
data = json.loads(response.text)
print(data)
