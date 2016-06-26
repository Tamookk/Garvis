# Garvis
Garvis (hard 'g') is a little digital assistant project of mine written in Python 2. (Hoping to move it over to Python 3 in the future). I have only tested Garvis on Windows platforms, but it should also work on Linux and macOS systems. An internet connection is also needed for Garvis to work properly.

Garvis can't do much, but it does work fine. It can do:
    
  - Speech recognition.
  - Speech synthesis.
  - Open the Google homepage in your system's default browser.
  - Grab weather conditions for my hometown.
  - Has a GUI if you don't want to use your voice.

### Version
1.0.0

### Third-Party Modules

Garvis uses a couple of third-party Python libraries, including:
  
  - [SpeechRecognition 3.4.6][sr] (Google Speech Recognition)
  - [pyttsx 1.1][pyttsx] (Text-to-Speech)

### Installation

I dunno, download and run it? I'm not so experienced with Python yet.

Garvis requires the two third-party libraries listed above, along with [Python 2][py2].


### Todos

  - Add ability to easily change location of weather
  - Fix bug where program crashes if closing out of window while Garvis is talking
  - Possibly change speech recognition engine from Google to something that works offline
 
   [sr]: <https://github.com/Uberi/speech_recognition>
   [pyttsx]: <https://github.com/parente/pyttsx>
   [py2]: <https://www.python.org/>