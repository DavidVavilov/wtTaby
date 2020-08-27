#wtTaby David Vavilov 2020
import os
import subprocess

class osFunctions:
    def getGUID():
        """
        A Function that generates an GUID from the powershell
        And returns it
        """
        powershellOutput = subprocess.check_output(['powershell.exe',"'{'+[guid]::NewGuid().ToString()+'}'"], shell=True)
        guid = powershellOutput.decode()
        guid = guid.replace("\r","")
        guid = guid.replace("\n","")
        return guid

    def searchForSettings():
        """
        A function that searches for the Microsoft Windows Terminal settings.json file
        """
        pathList = [] #List of paths that have the same name (settings.json)
        filename = "settings.json"
        search_path = str(input("Where to search (Example - 'c:/' , 'd:/'): "))
        print("Searching for settings.json .....")
        for root, dir, files in os.walk(search_path):
            if(filename in files):
                path = os.path.join(root, filename)
                if("Microsoft.WindowsTerminal" in path):
                    return path
                else:
                    pathList.append(path)

        if(len(pathList) > 0):
            for path in pathList:
                if("Microsoft.WindowsTerminal" in path):
                    return path
                    
        else:
            print("File not found...")




