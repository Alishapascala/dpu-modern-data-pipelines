import requests


API_KEY = "ee5e57aad461689637a35d18228ae307"
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}
url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=payload)
print(response.url)

data = response.json()
print(data)

