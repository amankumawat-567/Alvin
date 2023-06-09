import os
import re

def FindAll(query,substring):
    #Create list of all mainted folders in query in given sequence
    list = [query.find(substring)]
    i=0 
    while list[i] != -1:
        list.append(query.find(substring, list[i] + 1))
        i += 1
    return list

def CreateSearchLoaction(query):
    #convert natural language to folder path where to perform search
    strDirectory = query[query.find(" directory")-1]
    listFolder = FindAll(query," folder")
    listIN = FindAll(query," in ")
    path = strDirectory + "%3A%5C"
    if len(listIN) != len(listFolder):
        listFolder.insert(0,0)
    for i in range(len(listFolder)-2,0,-1):
        path += query[listIN[i-1]+4:listFolder[i]] + '%5C'
    return path

def QueriedFileName(query):
    #Find name for which user want to search ([file/folder name], [.extension] and [file.extension]) 
    try:
        match = re.search( r"search(?: for)? (\w+)(?: file| | folder)",query)
        name = match.group(1)
    except :
        try:
            match = re.search( r"search(?: for)? (\w+).(\w+)(?: file| )",query)
            name = f"{match.group(1)}.{match.group(2)}"
        except:
            match = re.search( r"search(?: for)? .(\w+)(?: files| | file)",query)
            name = f".{match.group(1)}"
    return name

def FileSearch(query,sysFolders):
    #Run a file search using windows file explorer search query 
    match = re.search(r" in (\w+)(?: folder|)",query)
    SearchPath = match.group(1)
    if SearchPath in sysFolders: #if user want to search in system folder
        SearchPath = "C%3A%5CUsers%5Camank%5C" + SearchPath
    else: #if user want to search in specific folder on pc
        SearchPath = CreateSearchLoaction(query)

    file_name = QueriedFileName(query) 
    os.startfile(f"search-ms:displayname=Search%20Results%20in%20New%20Volume%20(D%3A)&crumb=System.Generic.String%3A{file_name}&crumb=location:{SearchPath}")