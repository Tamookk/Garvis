from threading import Thread
from Tkinter import *
import pyttsx
import Queue
import speech_recognition as sr
import tkFont
import webbrowser

"""
Video sections have been commented out because it was just a dumb personal
video that it was playing, a test to see if it would work. Also my
internet speeds aren't nearly fast enough to upload a video.
"""

# Command list
google = ["Google", "navigate to Google", "search",  "open browser"]
#video = ["play video", "play a video", "open video", "open the video"]
weather = ["how's the weather", "weather"]
exiting = ["exit", "exit application", "quit", "goodbye"]

# Set up the TTS engine.
engine = pyttsx.init()
engine.setProperty('rate', 150)

# Grab voices and use the first one.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Sets up the main menu GUI.
class MainMenuGUI:
    """
    Set up the look for the GUI and the things that the buttons do.
    """
    def __init__(self, master):
        # Create a new frame (holder for widgets).
        frame = Frame(master)
        # Set frame background color.
        frame.configure(background="black")
        # Set up the font.
        self.font_Helvetica = tkFont.Font(family="Helvetica", size=12)

        # Add widgets.
        self.b_Google = Button(frame, text="Google", font=self.font_Helvetica, relief=FLAT, bg="white", command=self.runGoogleSearch)
        self.b_Weather = Button(frame, text="Weather", font=self.font_Helvetica, relief=FLAT, bg="white", command=self.getWeather)
        #self.b_Video = Button (frame, text="Video", font=self.font_Helvetica, relief=FLAT, bg="white", command=self.playVideoFile)

        # Pack the widgets.
        self.b_Google.pack(padx=10, pady=10)
        self.b_Weather.pack(padx=10, pady=10)
        #self.b_Video.pack(padx=10, pady=10)
        # Pack the frame.
        frame.pack()

    def runGoogleSearch(self):
        engine.say("Opening the Google homepage")
        webbrowser.open("https://www.google.com.au")

    """def playVideoFile(self):
        if engine._inLoop == True:
            engine.endLoop()

        engine.say("Playing a weirdo video.")
        engine.runAndWait()
        from os import startfile
        if sys.platform == 'win32':
            startfile("Resources\\Videos\\video.mp4")
        else:
            startfile("Resources/Videos/video.mp4")"""

    def getWeather(self):
        import os
        os.system("python WeatherGUI.py")

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = MainMenuGUI(master)

        # Set up the thread to do asynchronous speech recognition and synthesis.
        # More threads can also be created and used, if necessary.
        self.listening = True
        self.speechThread = Thread(target=self.speechRecognition)
        self.speechThread.start()

    def speechRecognition(self):
        engine.say("Hello Josh, what can I do for you today?")
        # Set up speech recogniser
        r = sr.Recognizer()
        # While listening.
        while self.listening:
            # Get commands.
            with sr.Microphone() as source:
                engine.runAndWait()
                audio = r.listen(source)
                print("Listening...")

                # Using Google speech recognition.
                spoken = r.recognize_google(audio)
                print(spoken)
                
                # Exit
                if spoken in exiting:
                    self.exitApplication()

                # Google
                elif spoken in google:
                    self.gui.runGoogleSearch()

                # Video
                #elif spoken in video:
                    #self.gui.playVideoFile()

                # Weather
                elif spoken in weather:
                    self.gui.getWeather()

                else:
                    engine.say("I'm sorry, I don't understand.")

    def exitApplication(self):
        engine.say("Goodbye Josh")
        engine.runAndWait()
        # Stop listening.
        self.listening = False
        # Exit application.
        root.quit()

# Set the root.
root = Tk()
# Set root title.
root.title("GARVISoft")
root.wm_iconbitmap('Resources/Images/icon.ico')
# Resizeable or not.
root.resizable(width=FALSE, height=FALSE)
# Set the minimum and only size of the window.
root.minsize(width=1280, height=720)
# Set background colour.
root.configure(background='black')

# Create a new instance of the threaded client.
client = ThreadedClient(root)
# Run the program
root.mainloop()

sys.exit()