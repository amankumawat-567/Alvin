from playsound import playsound
import threading
import re

def SetTimer(query):
    time = 0
    factor = 1

    for i in ["second","minute","hour"]:
        pattern = r"(\d+)\s+" + i +"?"
        match = re.search(pattern, query)
        if match :
            time += int(match.group(1))*factor
        factor *= 60

    Timer = threading.Timer(time,playsound,args=["res\Timer_notification.mp3"])
    Timer.start()