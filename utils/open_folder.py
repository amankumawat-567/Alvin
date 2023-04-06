import os

def FindAll(query,substring):
    #Create list of all mainted folders in query in given sequence
    list = [query.find(substring)]
    i=0 
    while list[i] != -1:
        list.append(query.find(substring, list[i] + 1))
        i += 1
    return list

def CreatePath(query):
    #convert natural language to folder path
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
    #Open a folder usind os module by passing its path
    try : # if folder user want to open is a system folder
        FolderPath = os.path.join(os.path.expanduser("~"), query.split(" ")[2])
    except : # if folder user want to open is some random folder on pc
        FolderPath = CreatePath(query)
    os.startfile(FolderPath)