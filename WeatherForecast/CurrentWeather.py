import requests
import pyfiglet
from simple_chalk import chalk


def current_weather_forecast():
    api_key = '93dafef5e89778b4c580394e585fc448'
    base_url='https://api.openweathermap.org/data/2.5/weather'

    weather_icons= {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
    }

    url = f"{base_url}?q=Riyadh&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code !=200:
        raise Exception("Please enter correct city or country")
    else:
        weather_forecast= response.json()
        city = weather_forecast["name"]
        temperature=weather_forecast["main"]["temp"]
        feels_like = weather_forecast["main"]["feels_like"]
        description = weather_forecast["weather"][0]["description"]
        icon = weather_forecast["weather"][0]["icon"]
        location = weather_forecast["sys"]["country"]

        weather_icon = weather_icons.get(icon, " ")
        output = f"{chalk.blue(pyfiglet.figlet_format(city, font='standard'))}, {chalk.magenta(location)}\n\n"
        output += f"{weather_icon}  {chalk.cyan(description)}\n"
        output += f"{chalk.green('Current temperature')}: {chalk.cyan(temperature)}°C\n"
        output += f"{chalk.green('Feels like')}: {chalk.cyan(feels_like)}°C"
        return output



