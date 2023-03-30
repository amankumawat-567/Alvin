import xml.etree.ElementTree as ET
import datetime
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

def strFindTime(query):
    time_pattern = r'\b(1[0-2]|[1-9]):([0-5][0-9])\s*([ap])\b'
    match = re.search(time_pattern, query)
    hour = int(match.group(1))
    minute = int(match.group(2))
    meridian = match.group(3)
    if meridian == 'p' and hour != 12:
        hour += 12
    elif meridian == 'a' and hour == 12:
        hour = 0
    Time = str(hour) + ":" + str(minute)
    return Time

def time_arr_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = ToSeconds(arr[0])
        less = [x for x in arr[1:] if ToSeconds(x) <= pivot]
        greater = [x for x in arr[1:] if ToSeconds(x) > pivot]
        return time_arr_quick_sort(less) + [arr[0]] + time_arr_quick_sort(greater)

def ActivateReminder(NextReminderTime,Reminders):
    ReminderTimer = threading.Timer(NextReminderTime, ReminderBeep, args=[Reminders])
    ReminderTimer.start()

def ToSeconds(time_str):
    time_parts = time_str.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    total_seconds = hours * 3600 + minutes * 60
    return total_seconds

def FindDelay(NextReminderTime):
    strToday = datetime.datetime.now().strftime("%H:%M")
    NextReminderTime = ToSeconds(NextReminderTime)-ToSeconds(strToday)
    return NextReminderTime

def ReminderBeep(Reminders):
    playsound("res\Reminder_notification.mp3")
    del Reminders[0]
    if len(Reminders)>0:
        NextReminderTime = Reminders[0]
        NextReminderTime = FindDelay(NextReminderTime)
        ActivateReminder(NextReminderTime,Reminders)

def AddReminder(xml_file,strReminderTime,Reminders):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    child = ET.Element("reminder")
    child.text = ""

    root.append(child)

    subchild = ET.Element("time")
    subchild.text = strReminderTime

    child.append(subchild)

    xml_string = ET.tostring(root)

    with open(xml_file, "wb") as f:
        f.write(xml_string)

    i = len(Reminders)
    if i > 0:
        i -= 1
        while i>=0 and ToSeconds(strReminderTime) < ToSeconds(Reminders[i]):
            i -= 1
        i += 1

    Reminders.insert(i,strReminderTime)
    if i == 0:
        delay = FindDelay(strReminderTime)
        ActivateReminder(delay,Reminders)

def GetReminders(xml_file,Reminders):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    strToday = datetime.datetime.now().strftime("%H:%M")
    stripTimeToday = datetime.datetime.strptime(strToday,"%H:%M").time()

    for elm in root.findall("./reminder/time"):
        stripTimeText = datetime.datetime.strptime(elm.text,"%H:%M").time()
        if stripTimeToday >= stripTimeText:
            ReminderPassed = root.find("./reminder/[time='"+ elm.text +"']")
            root.remove(ReminderPassed)
        else:
            Reminders.append(elm.text)

    xml_string = ET.tostring(root)    
    with open(xml_file, "wb") as f:
        f.write(xml_string)

    Reminders = time_arr_quick_sort(Reminders)
    
    if len(Reminders)>0:
        delay = FindDelay(Reminders[0])
        ActivateReminder(delay,Reminders)

    return Reminders