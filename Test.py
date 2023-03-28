import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#--------------------------------------
from utils.date_time import *
#--------------------------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

TimeObject = [" time"," date"," day"," year"," month"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your desktop assistant. How may I assist you?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)

    except Exception as e:
        print(e)
        return "None"
    return query

def work(query):
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Username\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif any(s in query for s in TimeObject):
            strTime = GetDateTime(query)    
            speak(strTime)

        elif 'quit' in query:
            speak("Quitting!")
            exit()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if query.startswith("Alvin"):
            print(f"User said: {query}\n")
            work(query.lower())

        