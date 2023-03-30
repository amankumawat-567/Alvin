import datetime

def Meridiem(strHour):
    Hr = eval(strHour)
    if Hr >= 12:
        Hr = str(Hr - 12)
        Mer = "p.m."
    else :
        Hr = str(Hr)
        Mer = "a.m."
    return Hr,Mer

WeekDay = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wedday",
    3 : "Thrusday",
    4 : "Friday",
    5 : "Satday",
    6 : "Sunday",
}

def GetTime(strToday):
    strHour = strToday.strftime("%H")
    strMinutes = strToday.strftime("%M")
    strHour,strMeridiem = Meridiem(strHour)
    strTime = strHour + ":" + strMinutes + " " + strMeridiem
    return strTime

def AddAND(res):
    if res != "":
        res = res + " "
    return res

def GetDateTime(query):
    strToday = datetime.datetime.now()
    res = ""
    if 'month' in query:
        res = strToday.strftime("%B")
    if 'date' in query:
        res = strToday.strftime("%d %B")
    if 'year' in query:
        res = AddAND(res) + strToday.strftime("%Y")
    if 'day' in query:
        res = AddAND(res) + WeekDay[datetime.date.today().weekday()]
    if 'time' in query:
        res = AddAND(res) + GetTime(strToday)
    return "it's " + res