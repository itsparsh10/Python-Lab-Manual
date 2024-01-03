import requests
import datetime

api_key = ""  # Your API key goes here
city = input("Enter city: ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=Metric")
weather_data = response.json()

if 'message' in weather_data:
    print("City not Found!")
else:
    print("\nCity:", city)
    print("Temperature:", weather_data['main']['temp'], "C")
    print("Humidity:", weather_data['main']['humidity'])
    
    sunrise_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    
    print("Sunrise(IST):", sunrise_time)
    print("Sunset(IST):", sunset_time)
