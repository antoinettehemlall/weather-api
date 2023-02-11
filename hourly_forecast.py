import requests
from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("WEATHER_API_KEY")

def get_weather(city, units='imperial', api_key=token):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
    r = requests.get(url)
    content = r.json()
    for dicty in content['list']:
        print(dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'])

print(get_weather(city='New York City'))