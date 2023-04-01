import os

def FindAll(query,substring):
    list = [query.find(substring)]
    i=0 
    while list[i] != -1:
        list.append(query.find(substring, list[i] + 1))
        i += 1
    return list

def CreatePath(query):
    strDirectory = query[query.find(" directory")-1]
    listFolder = FindAll(query," folder")
    listIN = FindAll(query," in ")
    finalDestination = query[11:listFolder[0]]
    path = strDirectory + ":\\"
    for i in range(len(listFolder)-2,0,-1):
        path += query[listIN[i-1]+4:listFolder[i]] + '\\'
    path += finalDestination
    return path


def OpenFolder(query):
    try :
        FolderPath = os.path.join(os.path.expanduser("~"), query.split(" ")[2])
    except :
        FolderPath = CreatePath(query)
    os.startfile(FolderPath)