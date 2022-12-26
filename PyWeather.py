# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['WeatherAPI']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

# explicit function to get
# weather details
def getweather(city):
	result = requests.get(url.format(city, api_key))
	
	if result:
		json = result.json()
		city = json['name']
		country = json['sys']['country']
		temp = json['main']['temp']
		weather = json['weather'][0]['main']
		final = [city, country, round(temp, 1), weather]
		return final
	else:
		print("No Content Found")

print(getweather("North Melbourne, AU"))