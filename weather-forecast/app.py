import requests
import json
import os

api_key = os.environ['ApiKey']
print(api_key)

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city = input('Enter the city: ').strip().lower()

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city


# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()



# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    main = x['main']

    current_temp = round(float(main['temp']) - 273.15)
    feels_like = round(float(main['feels_like']) - 273.15)
    current_pressure = main['pressure']
    current_humidity = main['humidity']
    weather = x['weather'][0]
    weather_description = weather['description']
    
    print(f'A previsão atual é {current_temp}ºC')
    print(f'A sensação térmica é de {feels_like}ºC')
    print(f'A pressão é de {current_pressure} hPa')
    print(f'A humidade atual é de {current_humidity}%')
    print(f'Clima: {weather_description}')
else:
    print('City not found!')