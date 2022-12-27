# import required modules
from configparser import ConfigParser
from datetime import datetime
import requests
import tkinter as tk

TUF = 1980
LOCATION = "North Melbourne, AU"
MINUTE_INTERVAL = 60

minute_to_ms = MINUTE_INTERVAL * 60000

# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['WeatherAPI']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

# Tkinter Window
window = tk.Tk()
window.geometry('625x270+'+ str(TUF) +'+400')
window.title("PyQuote")
window.configure(background='black')
window.overrideredirect(1)

# explicit function to get
# weather details
def getweather(city):
	result = requests.get(url.format(city, api_key))
	
	if result:
		json = result.json()

		temp = round(json['main']['temp'], 1)
		min = round(json['main']['temp_min'], 1)
		max = round(json['main']['temp_max'], 1)
		weather = json['weather'][0]['main']
		hum = json['main']['humidity']
		# Convert m/s to km/h
		wind = round(json['wind']['speed'] * 3.6, 1)

		final = [f'{temp} °C\n{min} °C\n{max} °C', f'{weather}\n{hum} %\n{wind} km/h']

		return final
	else:
		print("No Content Found")

# Update data every few minutes
def update():

	now = datetime.now()
	current_time = now.strftime("%I:%M %p")
	last_updated_label.config(text=">  " + current_time)

	weather_title.config(text=f'Temp: \nMin: \nMax: ')
	weather_label.config(text=getweather(LOCATION)[0])

	weather_title2.config(text=f'Sky: \nHumidity: \nWind Spd: ')
	weather_label2.config(text=getweather(LOCATION)[1])

	weather_title.after(int(minute_to_ms), update)


# UI
last_updated_label = tk.Label(window, font=("Minecraftia", 12), background="black", foreground="white", anchor="w")
last_updated_label.pack(side="top", anchor="ne", padx=10, pady=(5, 0))
location_label = tk.Label(window, font=("Minecraftia", 22), background="black", foreground="white", wraplength=590)
location_label.pack(padx=35, pady=(0, 12))
location_label.config(text="-  " + LOCATION + "  -")

data_box = tk.Label(window, background="black")
data_box.pack()

# Left Column
weather_title = tk.Label(data_box, font=("Minecraftia", 18), background="black", foreground="white", justify='right')
weather_title.pack(anchor="w", side=tk.LEFT)

weather_label = tk.Label(data_box, font=("Minecraftia", 18), background="black", foreground="white", justify='left')
weather_label.pack(anchor="w", padx=10, side=tk.LEFT)


# Right Column
weather_title2 = tk.Label(data_box, font=("Minecraftia", 18), background="black", foreground="white", justify='right')
weather_title2.pack(anchor="w",padx=(30, 0), side=tk.LEFT)

weather_label2 = tk.Label(data_box, font=("Minecraftia", 18), background="black", foreground="white", justify='left')
weather_label2.pack(anchor="w", padx=(10, 0), side=tk.LEFT)


update()

tk.mainloop()