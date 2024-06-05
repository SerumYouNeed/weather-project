import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city='Kielce'):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print('\n*** Get current weather conditions ***\n')
    city = input('\nPlease, enter a city name:\n')

    if not bool(city.strip()):
        city = "Kielce"
    
    # print(f'\nCurrent weather for {weather_data["name"]}.')
    # print(f'\nThe temperature is {weather_data["main"]["temp"]}.')
    # print(f'\nThe pressure is {weather_data["main"]["pressure"]} hPa.')
    weather_data = get_current_weather(city)
    pprint(weather_data)