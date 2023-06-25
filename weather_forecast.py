import requests
import json
import argparse
from datetime import datetime

# OpenWeatherMap API credentials
API_KEY = '1c65bc4200829863fbbf17989e4c4924' # Dummy API key

def get_weather(city):
    # API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    try:
        # Make a request to the API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        def time_format_for_location(utc_with_tz):
            local_time = datetime.utcfromtimestamp(utc_with_tz)
            return local_time.time()

        # Convert Kelvin to Celsius
        def kelvin_to_celsius(kelvin):
            celsius = kelvin - 273.15
            return celsius

        # Extract relevant weather information
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone = data['timezone']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        temp_in_celsius = kelvin_to_celsius(temperature)

        # Format the weather conditions with emojis
        formatted_weather = format_weather_conditions(weather)

        # Print the weather forecast
        print()
        print(f'Weather forecast for {city}:')
        print(f'Conditions: {formatted_weather}')
        print(f'Temperature: {temp_in_celsius:.2f}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed * 3.6:.2f} km/hr')
        print(f'Sunrise: {sunrise_time} hrs')
        print(f'Sunset: {sunset_time} hrs')

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f'Error: Invalid city name: {city}')
        else:
            print(f'Error: Failed to retrieve weather data. HTTPError: {err}')


#Define a function to format the weather conditions with emojis
def format_weather_conditions(weather):
    # Map weather conditions to emojis
    emoji_mapping = {
        'clear': '☀️',
        "few clouds" : "🌤️",
        'moderate rain': '🌦️',
        "scattered clouds" : "⛅",
        'rain': '🌧️',
        'snow': '❄️',
        'thunderstorm': '⛈️',
        'mist': '🌫️',
        "overcast clouds" : "☁️",
        "haze" : "🌫️",
        "broken clouds" : "🌥️",
    }

    # Check if any weather condition matches the mapping
    for condition, emoji in emoji_mapping.items():
        if condition in weather.lower():
            return f'{emoji} {weather}'

    # Return the original weather condition if no match found
    return weather


def get_air_quality(lat, lon, city):
    # API URL
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Get aqi from the data
        aqi = data['list'][0]['main']['aqi']

        aqi_emojis = {
            1: '😃',  # Good
            2: '🙂',  # Fair
            3: '😐',  # Moderate
            4: '😷',  # Poor
            5: '😖',  # Very Poor
        }

        if aqi == 1:
            aqi_status = 'Good'
        elif aqi == 2:
            aqi_status = 'Fair'
        elif aqi == 3:
            aqi_status = 'Moderate'
        elif aqi == 4:
            aqi_status = 'Poor'
        elif aqi == 5:
            aqi_status = 'Very Poor'
        else:
            aqi_status = 'Unknown'

        print(f'Latitude: {lat}')
        print(f'Longitude: {lon}')
        print(f'Air Quality Index: {aqi_status} {aqi_emojis.get(aqi)}')
        print()

    except Exception as err:
        print(f'Error: Failed to retrieve air quality data: {err}')


if __name__ == '__main__':
    # Parse the command-line arguments
    parser = argparse.ArgumentParser(description='Get the current weather forecast and air quality index for a city.')
    parser.add_argument('city', type=str, help='City name')
    args = parser.parse_args()

    # Retrieve the latitude and longitude coordinates for the city
    city_url = f'http://api.openweathermap.org/geo/1.0/direct?q={args.city}&limit=1&appid={API_KEY}'
    city_response = requests.get(city_url)
    city_data = city_response.json()

    if len(city_data) > 0:
        city_names = [city['name'].lower() for city in city_data]
        if any(args.city.lower() in city_name for city_name in city_names):
            city_index = next(index for index, city_name in enumerate(city_names) if args.city.lower() in city_name)
            city = city_data[city_index]
            latitude = city["lat"]
            longitude = city["lon"]

            # Get the weather forecast for the specified city
            get_weather(city['name'])

            # Get the air quality index for the specified city
            get_air_quality(latitude, longitude, city['name'])
        else:
            print(f'Error: Invalid city name: {args.city}')
    else:
        print(f'Error: Invalid city name: {args.city}')
