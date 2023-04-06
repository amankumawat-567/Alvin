import xml.etree.ElementTree as ET
import datetime
from playsound import playsound
import threading
import re

def strFindTask(query):
    # find [task] from query
    try:
        strTask = re.findall(r' for (.*) at',query)[0]
    except:
        strTask = re.findall(r' for (.*)',query)[0]
    return strTask

def strFindDate(query):
    # find [date] from query
    if 'today' in query:
        return datetime.datetime.now().strftime("%d %B")
    if 'tomorrow' in query:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%-d %B')
        return tomorrow
    try:
        date_pattern = r'\b\d{1,2}\s+[A-Z][a-z]{2,8}\b'
        strDate = re.findall(date_pattern, query)[0]
    except:
        strDate = datetime.datetime.now().strftime("%d %B")
    return strDate

def strFindTime(query):
    # find [time] from query
    time_pattern = r'\b(1[0-2]|[1-9]):([0-5][0-9])\s*([ap])\b'
    match = re.search(time_pattern, query)
    hour = int(match.group(1))
    minute = int(match.group(2))
    meridian = match.group(3)
    if meridian == 'p' and hour != 12:
        hour += 12
    elif meridian == 'a' and hour == 12:
        hour = 0
    strTime = str(hour) + ":" + str(minute)
    return strTime

def getReminderData(query):
    # create list of reminder date form query : [[date],[time],[task]]
    data = [strFindDate(query),strFindTime(query),strFindTask(query)]
    return data

def time_arr_quick_sort(arr):
    #Sort list of time using Quick Sort
    if len(arr) <= 1:
        return arr
    else:
        pivot = ToMinutes(arr[0])
        less = [x for x in arr[1:] if ToMinutes(x) <= pivot]
        greater = [x for x in arr[1:] if ToMinutes(x) > pivot]
        return time_arr_quick_sort(less) + [arr[0]] + time_arr_quick_sort(greater)
    
def ToMinutes(time_str):
    #convert string time to integer seconds
    time_parts = time_str.split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    total_seconds = hours * 60 + minutes
    return total_seconds

def FindDelay(NextReminderTime):
    #find time duration between current and upcoming reminder
    strToday = datetime.datetime.now().strftime("%H:%M")
    NextReminderTime = ToMinutes(NextReminderTime)-ToMinutes(strToday)
    return NextReminderTime

class reminder:
    # reminder object : it contain all upcooming reminders
    def __init__(self):
        self.Remind = {}
        self.Today = datetime.datetime.now().strftime("%d %B")
        self.TodyTask = []

    def __ActivateReminder(self,NextReminderTime):
        # activate a reminders
        ReminderTimer = threading.Timer(NextReminderTime*60, self.__ReminderBeep)
        ReminderTimer.start()

    def __ReminderBeep(self):
        # Beep sound on finshind the reminder and activate the next one if there
        playsound("res\Reminder_notification.mp3")
        print(self.Remind[self.Today][self.TodyTask[0]])
        del self.TodyTask[0]
        if len(self.TodyTask)>0:
            NextReminderTime = self.TodyTask[0]
            NextReminderTime = FindDelay(NextReminderTime)
            self.__ActivateReminder(NextReminderTime)

    def __Get_Today_tasks(self):
        # create all reminders for today and add them to TodayTask list
        if self.Today in self.Remind:
            self.TodyTask = list(self.Remind[self.Today].keys())
            self.TodyTask = time_arr_quick_sort(self.TodyTask)
            if len(self.TodyTask)>0:
                delay = FindDelay(self.TodyTask[0])
                self.__ActivateReminder(delay)

    def __switch_date(self):
        # add next day reminders to TodayTask list when a day overs
        self.Today = datetime.datetime.now().strftime("%d %B")
        self.__Get_Today_tasks()

    def GetReminders(self):
        # Get all reminders from Reminders.xml and add them to reminder object and dismiss all passed once
        Today = datetime.datetime.strptime(self.Today, '%d %B').date()
        Now = ToMinutes(datetime.datetime.now().strftime("%H:%M"))
        SwitchDateAfter = threading.Timer((1441 - Now)*60, self.__switch_date)
        SwitchDateAfter.start()

        tree = ET.parse("data\Reminders.xml")
        root = tree.getroot()

        for reminders in root.findall('reminder'):
            if datetime.datetime.strptime(reminders.get('date'), '%d %B').date() < Today:
                root.remove(reminders)
                continue
            if reminders.get('date') not in self.Remind:
                self.Remind[reminders.get('date')] = {}
            if ToMinutes(reminders[0].text) < Now:

                root.remove(reminders)
                continue
            else:
                self.Remind[reminders.get('date')][reminders[0].text] = reminders[1].text

        xml_string = ET.tostring(root)    
        with open("data\Reminders.xml", "wb") as f:
            f.write(xml_string)

        self.__Get_Today_tasks()
    
    def __AddReminder_to_Database(self,data):
        # add newly added reminders to Reminders.xml
        tree = ET.parse("data\Reminders.xml")
        root = tree.getroot()

        reminder = ET.Element("reminder")
        reminder.text = ""
        reminder.set("date",data[0])

        root.append(reminder)

        time = ET.Element("time")
        time.text = data[1]

        task = ET.Element("task")
        task.text = data[2]

        reminder.append(time)
        reminder.append(task)

        xml_string = ET.tostring(root)

        with open("data\Reminders.xml", "wb") as f:
            f.write(xml_string)
    
    def __update_todaytask(self,data):
        # update TodayTask list when a new reminder is added
        if data[0] == self.Today:
            i = len(self.TodyTask)
            if i > 0:
                strReminderTime = ToMinutes(data[1])
                i -= 1
                while i>=0 and strReminderTime < ToMinutes(self.TodyTask[i]):
                    i -= 1
                i += 1        
            if i == 0:
                ReminderTimer = threading.Timer(FindDelay(data[1]), playsound,args="res\Reminder_notification.mp3")
                ReminderTimer.start()
            else:
                self.TodyTask.insert(i,data[1])

    def AddReminder(self,data):
        # add new reminders
        if data[0] in self.Remind:
            if data[1] not in self.Remind[data[0]]:
                self.__AddReminder_to_Database(data)
                self.Remind[data[0]][data[1]] = data[2]
                self.__update_todaytask(data)
            else : 
                print("Reminders is already there...")
        else :
            self.__AddReminder_to_Database(data)
            self.Remind[data[0]] = {data[1]:data[2]}
            self.__update_todaytask(data)