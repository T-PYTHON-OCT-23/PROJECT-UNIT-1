import fontstyle
from simple_chalk import chalk
import CurrentWeather
from TemperatureConverter import temperatur_econverter
import Weather



text = fontstyle.apply('\nWelcome to Weather Forecast App: \n', 'bold/Italic/WHITE/BLUE_BG')
print(text)
Weather.history_search1()
while True:
    try:
        choise_number=input(fontstyle.apply('\nPlease choose among these options:\n1-Display the current weather forecast.\n2-Search for the weather forecast in a country or city.\n3-Temperature converter between Fahrenheit and Celsius.\n4-Exist: ', 'bold/Italic/BLUE'))
        if choise_number=='1':
            current_weather=CurrentWeather.current_weather_forecast()
            print(current_weather)
        elif choise_number=='2':
            while True:
                location=input(fontstyle.apply('\nEnter the country or city you want the weather forecast for: ', 'bold/Italic/WHITE'))
                weather_forecast=Weather.search_weather_forecast(location)
                print(weather_forecast)
                choise=input(fontstyle.apply('You want to continue searching ("yes" or "no"): ','bold/Italic/PURPLE'))
                if choise.lower()=='no':
                    break
                elif choise.lower()=='yes':
                    continue
                else:
                    raise TypeError('Invalid choise,try again')
        elif choise_number=='3':
            temperatur_econverter()
        elif choise_number=='4':
            print(fontstyle.apply('\nThank you for using Weather Forecast app','bold/Italic/WHITE/BLUE_BG'))
            break
        else:
            raise TypeError('Invalid choise,try again')
    except ValueError:
        print(chalk.red('Please Enter integer numbers'))
    except Exception as e:
        print(chalk.red(e))

    





