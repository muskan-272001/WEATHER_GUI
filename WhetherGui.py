import pytz
import requests
from tkinter import *
import tkinter.messagebox
import datetime

from timezonefinder import TimezoneFinder


def weather_data(city):
    res = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=b35975e18dc93725acb092f7272cc6b8&units"
                                                                     "=metric")
    w_data = res.json()
    print_weather(w_data)


def print_weather(result):
    try:
        a = (result['main']['temp'])
        b = (result['wind']['speed'])
        c = (result['weather'][0]['description'])
        d = (result['main']['temp_min'])
        e = (result['main']['temp_max'])
        f = (result['main']['pressure'])
        g = (result['main']['humidity'])
        lable_temp.config(text=a)
        lable_speed.config(text=b)
        lable_desc.config(text=c)
        lable_mintemp.config(text=d)
        lable_maxtemp.config(text=e)
        lable_pressure.config(text=f)
        lable_humid.config(text=g)
        tf = TimezoneFinder()
        longitude = (result['coord']['lon'])
        latitude = (result['coord']['lat'])
        # Timezone
        datez = tf.timezone_at(lng=longitude, lat=latitude)
        datez = str(datez)
        globaltime = datetime.datetime.now(pytz.timezone(datez))
        clock_1 = globaltime.strftime('%H:%M:%S')
        date_1 = globaltime.strftime('%A, %m/%d/%y')
        clock_label.config(text=clock_1)
        date_label.config(text=date_1)
    except:
        var = result['cod'] == '404' and result['message'] == 'city not found'
        tkinter.messagebox.showerror(title="error", message="City Name not found")


root = tkinter.Tk()
root.geometry("1500x900")
root.title("Weather App")
p1 = PhotoImage(file="C:\\Users\\Ritu\\Desktop\\icon.png")
# Setting icon of master window
root.iconphoto(False, p1)
bg = PhotoImage(file="C:\\Users\\Ritu\\Desktop\\re.png")
# Show image using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

lable_0 = Label(root, text="  WEATHER FORECAST  ", anchor='e', font=("comic sans", 48, "bold",), bg=None, fg='black',
                bd=7, relief='flat')
lable_0.place(x=300, y=30)

city_name = StringVar()
entry_1 = Entry(root, font=("arial", 23), bg='white', textvariable=city_name, width=24)
entry_1.place(x=700, y=160)

lable_7 = Label(root, text="Enter the city name ", width=20, font=("comic sans", 23, "bold"), bg='light yellow',
                fg='grey2', borderwidth=3, relief="raised")
lable_7.place(x=200, y=160)

lable_1 = Label(root, text=" Minimum Temperature : ", width=20, font=("comic sans", 17), fg='black',
                bg='light yellow', borderwidth=3, relief="raised")
lable_1.place(x=110, y=310)

lable_6 = Label(root, text="Maximum Temperature : ", width=20, font=("comic sans", 17), fg='black',
                bg='light yellow', borderwidth=3, relief="raised")
lable_6.place(x=110, y=380)

lable_2 = Label(root, text="Temperature : ", width=20, font=("comic sans", 17), fg='black', bg='light yellow',
                borderwidth=3, relief="raised")
lable_2.place(x=110, y=450)

lable_3 = Label(root, text="Wind Speed : ", width=20, font=("comic sans", 17), fg='black', bg='light yellow',
                borderwidth=3, relief="raised")
lable_3.place(x=750, y=310)

lable_5 = Label(root, text="Humidity : ", width=20, font=("comic sans", 17), fg='black', bg='light yellow',
                borderwidth=3, relief="raised")
lable_5.place(x=750, y=380)

lable_8 = Label(root, text="Pressure : ", width=20, font=("comic sans", 17), fg='black', bg='light yellow',
                borderwidth=3, relief="raised")
lable_8.place(x=750, y=450)

lable_9 = Label(root, text=" Description :", width=20, font=("comic sans", 17), fg='black', bg='light yellow',
                borderwidth=3, relief="raised")
lable_9.place(x=320, y=540)

lable_mintemp = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_mintemp.place(x=460, y=310)

lable_maxtemp = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_maxtemp.place(x=460, y=380)

lable_temp = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_temp.place(x=460, y=450)

lable_speed = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_speed.place(x=1030, y=310)

lable_humid = Label(root, text="...", width=7, bg='white', font=("bold", 25), fg='black')
lable_humid.place(x=1030, y=380)

lable_pressure = Label(root, text="...", width=12, bg='white', font=("bold", 17), fg='black')
lable_pressure.place(x=1030, y=450)

lable_desc = Label(root, text="...", width=24, bg='white', font=("bold", 17), fg='black')
lable_desc.place(x=693, y=540)

btn = Button(root, text="SUBMIT", width=15, font=("comic sans", 13), bg='maroon', fg='white', bd=9,
             command=lambda: weather_data(entry_1.get())).place(x=590, y=235)
clock_label = Label(root, width=15, font=("comic sans", 20, "bold",), bg='white', fg='black',
                    bd=7)
clock_label.place(x=690, y=650)
date_label = Label(root, width=15, font=("comic sans", 20, "bold",), bg='white', fg='black',
                   bd=7)
date_label.place(x=400, y=650)

root.mainloop()
