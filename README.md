# Weather Forecasting Tool 🌞
The Weather Forecast CLI Tool is a command-line utility that enables users to fetch and display the current weather forecast for a specific city. By leveraging the OpenWeatherMap API, this tool provides accurate and up-to-date weather data for effective planning of outdoor activities, travel arrangements, and day-to-day decision making.
Implemented in Python, the WeatherForecast CLI Tool offers a streamlined interface for easy usage. Users can simply enter the desired city name, and the tool will retrieve and present comprehensive weather information.

## Features
- Fetches weather data using the [OpenWeatherMap API](https://openweathermap.org/api)
- Retrieves current weather forecast for a specific city
- Command-line interface for quick and convenient access

## Technologies Used

- Python: A versatile and popular programming language that enables efficient data manipulation and parsing.
- GitHub Copilot: An AI-powered coding assistant that aids in API usage, data parsing, and error handling.
- OpenWeatherMap API: A comprehensive weather data API offering a wide range of weather information for locations worldwide.

## GitHub Copilot Integration

GitHub Copilot plays a significant role in the development of this tool. It assists in various aspects, including:

- API Usage: GitHub Copilot generates API requests, including the endpoint, parameters, and authentication, simplifying integration with the OpenWeatherMap API.
- Data Parsing: Copilot provides suggestions and code snippets for parsing the JSON responses from the OpenWeatherMap API, making it easier to extract the relevant weather data.
- Error Handling: GitHub Copilot offers guidance on implementing error handling mechanisms, such as exception handling and error status code checks, ensuring a robust and reliable tool.

## Usage

To use the Weather Forecasting Tool, follow these steps:

1. Clone the repository from GitHub.
2. Install the below dependencies/libraries.

```py
> pip install requests
> pip install argparse
```
3. Create a free account on [OpenWeatherMap](https://openweathermap.org) and obtain an API key. Paste the API Key in place of the dummy API_KEY variable.

4. Furthermore you can create a ```.env``` and add it to ```.gitignore``` file to store the API Key secretly.

5. Run the command-line tool and provide the name of the City for which you want to retrieve the Weather Forecast.

```py
# cd into the WeatherApp folder
# run the below command by adding the desired city-name 
> python weather_forecast.py <city-name>

# Example
> python weather_forecast.py Delhi

# wrap city name in quotes if it contains spaces
> python weather_forecast.py "New Orleans"
```

6. The tool will fetch the weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and displays the current forecast for the specified city.

# Examples
❮img src="Commandlineexamples/example1.png"❯
   
