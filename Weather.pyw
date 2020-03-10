import time
import pyowm
import configparser
from tkinter import *
from tkinter.ttk import *
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

def get_weather(key, location):
    observe = key.weather_at_place(location)
    weather = observe.get_weather()
    currentWeather = weather.get_detailed_status()
    wind = weather.get_wind()
    humidity = weather.get_humidity()
    temp = weather.get_temperature("celsius")

    imageUrl = weather.get_weather_icon_url()
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((125, 125), Image.ANTIALIAS)  # (height, width)
    photo = ImageTk.PhotoImage(im)
    WeatherImagelbl.configure(image=photo)
    WeatherImagelbl.image = photo

    WeatherInfolbl.configure(text=f"Weather: {currentWeather}\nWind Speed: {wind['speed']}\nHumidity: {humidity}%\n"
                                  f"{temp['temp_max']}°C")
    WeatherInfolbl2.configure(text=f"   {temp['temp_min']}°C")
    timelbl.configure(text=time.strftime("%H:%M"))

def clicked(event):
    answer = entry.get().title()
    titlelbl.configure(text=answer)
    get_weather(owm, answer)

api_key = get_api_key()
owm = pyowm.OWM(api_key)
window = Tk()
window.title("Weather App")
window.geometry("600x400")
topFrame = Frame(window)
topFrame.pack()

timelbl = Label(topFrame, text=time.strftime("%H:%M"), font=("Arial Bold", 20))
titlelbl = Label(topFrame, text="Type in a city", font=("Arial Bold", 50))
entry = Entry(topFrame)
entry.bind("<Return>", clicked)
WeatherInfolbl = Label(topFrame, font=("Arial", 20))
WeatherInfolbl2 = Label(topFrame, font=("Arial", 10))
WeatherImagelbl = Label(topFrame)

timelbl.pack()
titlelbl.pack()
entry.pack()
WeatherImagelbl.pack(side=LEFT)
WeatherInfolbl.pack()
WeatherInfolbl2.pack(side=LEFT)
window.mainloop()
