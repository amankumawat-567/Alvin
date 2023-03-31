import os
import subprocess
import glob
import xml.etree.ElementTree as ET

def AddSearchToDatabase(xml_file,app_name,file_path):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    child = ET.Element("App")
    child.text = ""

    root.append(child)

    subchild = ET.Element("Name")
    subchild.text = app_name

    child.append(subchild)

    subchild = ET.Element("Path")
    subchild.text = file_path

    child.append(subchild)

    xml_string = ET.tostring(root)

    with open(xml_file, "wb") as f:
        f.write(xml_string)

def SearchDatabase(app_name,xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elm in root.findall("./App"):
        if app_name in elm.find("Name").text.lower() :
            return elm.find("Path").text
    return 0

def FindPath(app_name,xml_file):
    app_path = SearchDatabase(app_name,xml_file)

    if app_path == 0:
        result = subprocess.run(['powershell', 'Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, InstallLocation'], capture_output=True, text=True)
        app_path = ""

        for line in result.stdout.strip().split('\n'):
            if app_name in line.lower():
                app_name = line.split("C:")[0].strip() 
                app_path = "C:" + line.split("C:")[1].strip()
                break

        if app_path != "":
            file_list = glob.glob(app_path + '/*.exe')
            if file_list == []:
                file_list = glob.glob(app_path + '/*')
                for file_path in file_list:
                    j = file_path[len(app_path)+1:]
                    if j.lower() in app_name.lower():
                        app_path = file_path
                        j = "changed"
                        break
                if j != "changed":
                    app_path += "\\bin"                

            file_list = glob.glob(app_path + '/*.exe')
            for file_path in file_list:
                    j = (file_path)[len(app_path)+1:-4]
                    if j.lower() in app_name.lower():
                        AddSearchToDatabase(xml_file,app_name,file_path)
                        return file_path

        else:
            print("opps! You system don't know this app path")

    else:
        AddSearchToDatabase(xml_file,app_name,file_path)
        return app_path


def LaunchApp(app_name,xml_file):
    try :
        subprocess.run(app_name)
    except :
        app_path = FindPath(app_name,xml_file)
        os.startfile(app_path)