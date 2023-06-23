# Weather Forecasting Tool
This is a command-line tool that fetches and displays the current weather forecast for a specific city. It leverages the OpenWeatherMap API to retrieve weather data and utilizes Python for data parsing and manipulation. The purpose of this tool is to provide an easy and efficient way to access accurate and up-to-date weather information, allowing users to plan their outdoor activities, travel, and day-to-day decision making.

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

- API Usage: GitHub Copilot generates API requests, including the endpoint, parameters, and authentication, simplifying integration with the WeatherAPI.com API.
- Data Parsing: Copilot provides suggestions and code snippets for parsing the JSON or XML responses from the WeatherAPI.com API, making it easier to extract the relevant weather data.
- Error Handling: GitHub Copilot offers guidance on implementing error handling mechanisms, such as exception handling and error status code checks, ensuring a robust and reliable tool.

## Usage

To use the Weather Forecasting Tool, follow these steps:

1. Clone the repository from GitHub.
2. Install the below dependencies/libraries.

```py
> pip install requests
> pip install argparse
```
4. Create a free account on [WeatherAPI.com](https://www.weatherapi.com/) and obtain an API key. Paste the API Key in the .env file.

```py
# .env file
API_KEY=<your-api-key>
```

4. Run the command-line tool and provide the name of the city for which you want to retrieve the weather forecast.

```py
# cd into the weathercli folder
cd weathercli
python -m weathercli forecast <city-name>

# Example
python -m weathercli forecast London

# wrap city name in quotes if it contains spaces
python -m weathercli forecast "New York"
```

5. The tool will fetch the weather data from the WeatherAPI.com API and display the current forecast for the specified city.
