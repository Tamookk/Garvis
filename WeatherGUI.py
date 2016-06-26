from Tkinter import *
from PIL import ImageTk, Image
import json
import pyttsx
import tkFont
import urllib
import urllib2

degree_sign= u'\N{DEGREE SIGN}'

url = "http://api.openweathermap.org/data/2.5/weather?q={moss%20vale}&units=metric&APPID=6b516617129f49f13280b938f8267175"
result = urllib2.urlopen(url).read()
data = json.loads(result)

conditions = data['name'] + " - " + str(data['main']['temp']) + degree_sign + "C - " + data['weather'][0]['description']
coords = str(data['coord']['lat']) + degree_sign + "N\n" + str(data['coord']['lon']) + degree_sign + "E\n"
pressure = str(data['main']['pressure']) + "hPa"
humidity = str(data['main']['humidity']) + "% Humidity"
wind = str(data['wind']['speed']) + "km/h Wind at " + str(data['wind']['deg']) + degree_sign
moreInfo = coords + "\n" + pressure + "\n" + humidity + "\n" + wind + "\n"

from os import startfile
if sys.platform == 'win32':
    imageIcon = "Resources\\Images\\" + data['weather'][0]['icon'] + ".gif"
else:
    imageIcon = "Resources/Images/" + data['weather'][0]['icon'] + ".gif"

# Set up the TTS engine.
engine = pyttsx.init()
engine.setProperty('rate', 150)

# Grab voices and use the first one.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Sets up the main menu GUI.
class WeatherGUI:
    """
    Set up the look for the GUI and the things that the buttons do.
    """
    def __init__(self, master):
        # Create a new frame (holder for widgets).
        frame = Frame(master)
        # Set frame background color.
        frame.configure(background="black")
        # Set up the font.
        self.font_Helvetica = tkFont.Font(family="Helvetica", size=18)
        self.font_Helvetica_Smaller = tkFont.Font(family="Helvetica", size=14)

        self.Icon = ImageTk.PhotoImage(Image.open(imageIcon))

        self.l_Weather = Label(text=conditions, font=self.font_Helvetica, fg='white', bg='black')
        self.l_MoreInfo = Label(text=moreInfo, font=self.font_Helvetica_Smaller, fg='white', bg='black')
        
        self.l_WeatherImage = Label(image=self.Icon)

        self.b_Close = Button(text="Close", font=self.font_Helvetica, relief=FLAT, bg="white", command=master.quit)

        self.l_Weather.pack(padx=10, pady=10)
        self.l_MoreInfo.pack(padx=10, pady=10)
        self.l_WeatherImage.image = self.Icon
        self.l_WeatherImage.pack(padx=10, pady=10)
        self.b_Close.pack(padx=10, pady=10)


# say the weather
def sayWeather():
    engine.say("The weather in " + data['name'] + " is " + str(data['main']['temp']) + " degrees celsius, and conditions are " + data['weather'][0]['description'])
    engine.runAndWait()

# Set the root.
root = Tk()
# Set root title.
root.title("GARVISoft - Weather")
root.wm_iconbitmap('Resources/Images/icon.ico')
# Resizeable or not.
root.resizable(width=FALSE, height=FALSE)
# Set the minimum and only size of the window.
root.minsize(width=300, height=720)
# Set background colour.
root.configure(background='black')

weather = WeatherGUI(root)

root.after(1000, sayWeather)

# Run the program
root.mainloop()