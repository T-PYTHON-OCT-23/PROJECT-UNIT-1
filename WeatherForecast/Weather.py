import requests
import pyfiglet
import fontstyle
from simple_chalk import chalk
import json
history_search=[]


def search_weather_forecast(location):
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

    url = f"{base_url}?q={location}&appid={api_key}&units=metric"
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
        weather_icon = weather_icons.get(icon)
        item={
            'City':city,
            'weather_icon':weather_icon,
            'temperature':temperature
        }

        found_city =  list(filter(lambda history: history['City'] == item['City'], history_search))
        if len(found_city) == 0:
            history_search.append(item)
            with open("history_search.json", "w", encoding="utf-8") as file:
                content = json.dumps(history_search)
                file.write(content)
        output = f"{chalk.blue(pyfiglet.figlet_format(city,font='standard'))}, {chalk.magenta(location)}\n\n"
        output += f"{weather_icon}  {chalk.cyan(description)}\n"
        output += f"{chalk.green('Temperature')}: {chalk.cyan(temperature)}°C\n"
        output += f"{chalk.green('Feels like')}:{chalk.cyan(feels_like)}°C\n"
        return output
def location_search():
    print(fontstyle.apply('Your last location search is: ','bold/Italic/PURPLE'))
    with open("history_search.json", "r", encoding="utf-8") as file:
        content = file.read()
        history_search = json.loads(content)
    for item in history_search:
        print(item['City'],' '+item['weather_icon']+' ',item['temperature'])

    

