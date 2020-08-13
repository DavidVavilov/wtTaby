#wtTaby David Vavilov 2020
"""
An module for the tabyFunctions
"""
import json 
from osFunctions import osFunctions

class tabyFunctions:    
    def setup():
        """
        Setup the wtTaby program with a path to the
        Microsoft Windows Terminal settings.json file
        and a profile name
        """
        jsonSetup = {
            'settingsPath' :'',
            'profileName' :''
        }

        try: #Checks if there si already a setup file
            checkFile = open('tabySetup.json','r')
            print("wtTaby setup already exists!")
            jsonFile = json.load(checkFile)
            print("Path -",jsonFile['settingsPath'])
            print("Profile name -",jsonFile['profileName'])
            
        except FileNotFoundError: #If false, Creates a new one
            print("***Before setup, Remove comments in the setting.json file to not cause trouble to the program***")
            pathOfSettings = input("Enter the path of the Microsoft Windows Terminal settings: ")
            jsonSetup['settingsPath'] = pathOfSettings
            profileName = input('Enter profile name: ')
            jsonSetup['profileName'] = profileName
            print("wtTaby setup completed!!")
            setupFile = open('tabySetup.json','w')
            json.dump(jsonSetup, setupFile, indent=2)

    def autoSetup():
        """
        Setup the wtTaby program (auto) with a path to the
        Microsoft Windows Terminal settings.json file
        and a profile name
        """
        jsonSetup = {
            'settingsPath' :'',
            'profileName' :''
        }

        try: #Checks if there si already a setup file
            checkFile = open('tabySetup.json','r')
            print("wtTaby setup already exists!")
            jsonFile = json.load(checkFile)
            print("Path -",jsonFile['settingsPath'])
            print("Profile name -",jsonFile['profileName'])
            
        except FileNotFoundError: #If false, Creates a new one
            print("***Before setup, Remove comments in the setting.json file to not cause trouble to the program***")
            settingsPath = osFunctions.searchForSettings()
            
            if(settingsPath != None): #Checks if path found
                print("Found path - ", settingsPath)
                jsonSetup['settingsPath'] = settingsPath
                profileName = input('Enter profile name: ')
                jsonSetup['profileName'] = profileName
                print("wtTaby setup completed!!")
                setupFile = open('tabySetup.json','w')
                json.dump(jsonSetup, setupFile, indent=2)
            else:
                print("Can't find 'settings.json'")


    def newTaby():
        """
        Add new Tabs 
        """
        filePath = "testing.json"
        terminalSettingsFileRead = open(filePath,'r')
        string = terminalSettingsFileRead.read()
        data = json.loads(string)
        tabyDict = {
            'guid': "",
            'name': "",
            'commandline':""
        }
        guid = osFunctions.getGUID() #Gets the GUID from the powershell
        print('GUID generated -',guid)
        tabName = input("Enter tab name: ")
        commandLine = input("Enter a commandline: ")
        tabyDict['guid'] = guid
        tabyDict['name'] = tabName
        tabyDict['commandline'] = commandLine

        data['profiles']['list'].append(tabyDict)

        terminalSettingsFile = open(filePath,'w')
        json.dump(data, terminalSettingsFile, indent=4)
        print(tabName,"Taby Added to the Windows Terminal!")


    def printTabs(): 
        """
        Shows the tabs that are in the settings.json file
        """
        setupFile = open('tabySetup.json','r')
        jsonFile = json.load(setupFile)
        filePath = jsonFile['settingsPath']

        terminalSettingsFile = open(filePath,'r')
        string = terminalSettingsFile.read()
        data = json.loads(string)
        for profile in data['profiles']['list']:
            print("GUID -" ,profile['guid'])
            print("Tab Name -" ,profile['name'])
            print("---------------------------")
           
    def setDefault():
        filePath = "testing.json"
        terminalSettingsFileRead = open(filePath,'r')
        string = terminalSettingsFileRead.read()
        data = json.loads(string)
        print(data['defaultProfile'])


    def help():
        print("wtTaby - Help menu!")
        print("To run: wtTaby [FUNCTION] [OPERATOR(If needed)]")
        print("Functions - ")
        print("Setup - \n '--setup' : To setup the system, Add '-a' to auto search for the settings file")
        print("New Tab - \n '--newTaby' : To add a new tab")
        print("Show - \n '--show' : Shows the tabs that are in the settings.json file")

