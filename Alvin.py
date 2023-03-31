import pyttsx3
import speech_recognition as sr
import webbrowser

#--------------------------------------
from utils.date_time import *
from utils.reminders import *
from utils.app_launcher import *
#--------------------------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

TimeObject = ["time","date","day","year","month"]
ReminderObject = ["set reminder","remind me"]
TimerObject = ["set timer","remind me after"]
QuitingObject = ["quit","exit","shutdown","sleep","off","turn off"]


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

def work(query,Reminders):
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open' in query:
            app_name = query[11:]
            speak(f"opening {app_name}")
            LaunchApp(app_name,"data\pre_searches_app_url.xml")

        elif any(s in query for s in TimerObject):
            SetTimer(query)   
            if TimerObject[0] in query:
                speak("Timer set")
            else:
                speak("Okay I'll remind you")

        elif any(s in query for s in TimeObject):
            strTime = GetDateTime(query)    
            speak(strTime)

        elif any(s in query for s in ReminderObject):
            strReminderTime = strFindTime(query)
            AddReminder('data\Reminders.xml',strReminderTime,Reminders)    
            speak("Okay I'll remind you")

        elif any(s in query for s in QuitingObject):
            speak("Quitting!")
            exit()

        else:
            speak("Sorry I didn't get what you want to say")

if __name__ == "__main__":
    wishMe()
    Reminders = []
    Reminders = GetReminders('data\Reminders.xml',Reminders)
    while True:
        query = takeCommand()
        if query.startswith("Alvin"):
            print(f"User said: {query}\n")
            work(query.lower(),Reminders)
            