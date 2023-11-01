import fontstyle
def temperatur_econverter():
    unit=input(fontstyle.apply('\nEnter a unit to convert ("C" for Celsius or "F" for Fahrenheit): ','bold/Italic/WHITE'))
    if unit.lower()=='f':
        temperatur1=int(input(fontstyle.apply('Enter a temperatur in Celsius: ','bold/Italic/WHITE')))
        fahrenheit = lambda celsius:round((celsius * 9/5 )+ 32,2) 
        print(fontstyle.apply(F'The temperatur in fahrenheit: {fahrenheit(temperatur1)} F','bold/Italic/GREEN'))
    elif unit.lower()=='c':
        temperatur2=int(input(fontstyle.apply('Enter a temperatur in Fahrenheit: ','bold/Italic/WHITE')))
        celsius=lambda fahrenheit:round((fahrenheit - 32) * 5/9,2)
        print(fontstyle.apply(F'The temperatur in celsius: {celsius(temperatur2)} C','bold/Italic/GREEN'))
    else:
        raise TypeError('invalid unit,try again')

        


