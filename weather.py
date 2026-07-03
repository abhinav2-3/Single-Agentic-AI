from dotenv import load_dotenv
import os
import requests
from langchain.tools import tool

load_dotenv()

WEATHER_API_KEY: str | None = os.getenv("WEATHER_API_KEY")


@tool
def get_weather_data(city: str) -> str:
    """Get current weather data for a given city."""
    url = f"https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}"

    response = requests.get(url)
    data = response.json()

    if "current" not in data:
        return f"Data is not found for {city} city."

    return (
        f"City: {city}\n"
        f"Temperature: {data['current' ] ['temperature' ]}℃\n"
        f"Weather: {data['current' ] ['weather_descriptions' ] [0]} \n"
        f"Humidity: {data['current']['humidity' ]}%"
    )
