#Importing Built-in Modules
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
#Importing feature Modules
from utils.date_time import *
from utils.reminders import *
from utils.timer import *
from utils.app_launcher import *
from utils.file_search import *
from utils.open_folder import *
#--------------------------------------

#create a pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#List of words to recognise specific command
TimeObject = ["time","date","day","year","month"]
ReminderObject = ["set reminder","remind me"]
TimerObject = ["set timer","remind me after"]
QuitingObject = ["quit","exit","shutdown","sleep","off","turn off"]
sysFolders = ["desktop","documents","downloads","music","pictures","videos"]

def speak(audio):
    #text to speech function
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    #Function : Alvin will greet its user
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your desktop assistant. How may I assist you?")
 
def takeCommand():
    #speech to text function
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
        #This Function will recognise what task to do and will execute them
        
        # web search
        if (' search ' in query):
            if query[-6:] == "google":
                speak("googling it")
                pattern = r'search(?: for|) (.*)(?: on| in| at) google'
                match = re.search(pattern, query)
                search_query = match.group(1)
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif query[-7:] == "youtube":
                speak("searching youtube")
                pattern = r'search(?: for|) (.*)(?: on| in| at) youtube'
                match = re.search(pattern, query)
                search_query = match.group(1)
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
            else:
                try:
                    FileSearch(query,sysFolders)
                except:
                    speak("Sorry I didn't get that")

        #Open website (google and youtube)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        #Open a folder on pc
        elif (" directory" in  query) or any(s in query for s in sysFolders):
            try:
                OpenFolder(query)
                speak("Opening")
            except:
                speak("Sorry I can't find")

        #Open a app
        elif 'open' in query:
            app_name = query[11:]
            speak(f"opening {app_name}")
            LaunchApp(app_name,"data\pre_searches_app_url.xml")

        #Set a Timer
        elif any(s in query for s in TimerObject):
            SetTimer(query)   
            if TimerObject[0] in query:
                speak("Timer set")
            else:
                speak("Okay I'll remind you")

        # tell Date and time
        elif any(s in query for s in TimeObject):
            strTime = GetDateTime(query)    
            speak(strTime)

        #Set Reminder
        elif any(s in query for s in ReminderObject):
            Reminderdata = getReminderData(query)
            Reminders.AddReminder(Reminderdata)  
            speak("Okay I'll remind you")

        # close Alvin
        elif any(s in query for s in QuitingObject):
            speak("Quitting!")
            exit()

        # Wikipedia search for query
        else:
            try:
                speak("according to wikipedia " + wikipedia.summary(query[6:], sentences=2))
            except:
                #if not able to figure out what user said    
                speak("Sorry I didn't get what you want to say")

if __name__ == "__main__":
    wishMe()

    #created a reminder object
    Reminders = reminder()

    #fatched all reminders from Reminders.xml
    Reminders.GetReminders()

    #Main
    while True:
        query = takeCommand()
        if query.startswith("Alvin"):
            print(f"User said: {query}\n")
            work(query.lower(),Reminders)
            