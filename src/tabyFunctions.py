#wtTaby - David Vavilov 2020
"""
An module for the tabyFunctions
"""
import json 
from osFunctions import osFunctions


class tabyFunctions: 
    """
    A class of functions that relate
    to the wtTaby system
    """   
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
            tabyFunctions.saveTabs()

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
                tabyFunctions.saveTabs() #Saves the tabs into the 'tabs.json' file
            else:
                print("Can't find 'settings.json'")


    def newTaby():
        """
        Add new Tabs to the 'settings.json' and saves the tab into the 'tabs.json' file
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
        terminalSettingsFile.close()
        tabyFunctions.saveTabs() #Saves the tabs into the 'tabs.json' file

    def saveTabs():
        """
        Saves the Tabs from the 'settings.json' file
        into a new json file called 'tabs.json'
        """
        try:
            #setupFile = open('tabySetup.json','r')
            #jsonFile = json.load(setupFile)
            #filePath = jsonFile['settingsPath']
            #terminalSettingsFile = open(filePath,'r')
            tabsDict = { "tabs" : []}
            terminalSettingsFile = open("testing.json",'r')
            tabsJSONFile = open("tabs.json",'w')
            string = terminalSettingsFile.read()
            data = json.loads(string)
            for profile in data['profiles']['list']:
                dictExample = {"GUID" : "", "tabName" : ""}
                dictExample["GUID"] = profile['guid']
                dictExample["tabName"] = profile['name']
                tabsDict["tabs"].append(dictExample)
            
            json.dump(tabsDict,tabsJSONFile, indent=4)
            
        
        except Exception as error:
            print(error)

    

    def printTabs(): 
        """
        Shows the tabs that are in the settings.json file
        """
        try:
            #setupFile = open('tabySetup.json','r')
            #jsonFile = json.load(setupFile)
            #filePath = jsonFile['settingsPath']

            #terminalSettingsFile = open(filePath,'r')
            terminalSettingsFile = open("testing.json",'r')
            string = terminalSettingsFile.read()
            data = json.loads(string)
            print("Windows Terminal Tabs - ")
            for profile in data['profiles']['list']:
                print("GUID -" ,profile['guid'])
                print("Tab Name -" ,profile['name'])
                print("---------------------------")
        
        except Exception as error:
            print(error)
           
    def setDefault():
        """
        Sets a new default tab
        """
        filePath = "testing.json"
        terminalSettingsFileRead = open(filePath,'r')
        tabsFile = open('tabs.json','r')
        jsonTabs = json.load(tabsFile)
        string = terminalSettingsFileRead.read()
        terminalSettingsFileRead.close()
        data = json.loads(string)
        for tab in jsonTabs['tabs']:
            if(tab['GUID'] ==  data['defaultProfile']):
                defaultTabName = tab['tabName']
            
        print(f"Your Default tab is : Name - {defaultTabName}, GUID - {data['defaultProfile']},")
        newDefaultTab = input("What tab would you like to be the default?")
        getGuid = None
        for tab in jsonTabs['tabs']:
            if(tab['tabName'] ==  newDefaultTab):
                getGuid = tab['GUID']
        
        if(getGuid is not None):
            terminalSettingsFileWrite = open(filePath,'w')
            data['defaultProfile'] = getGuid
            try:
                json.dump(data,terminalSettingsFileWrite, indent=4)
                print("New Default tab has been set!!")
            except Exception as error:
                print(error)
        else:
            print("Tab not found!")

        
    def editTaby(tabyName):
        """
        A function that gets a name of a tab and allows
        the user to edit that tab
        Input: tabyName (Name of the tab)
        """
        foundTabs = []
        tabsFile = open("tabs.json",'r')
        tabs = json.load(tabsFile)
        for tab in tabs["tabs"]:
            if(tabyName.lower() == tab["tabName"].lower()):
                foundTabs.append(tab)

        if(len(foundTabs) > 1):
            print(f"Found {len(foundTabs)} tabs - ")
            for foundTab in foundTabs:
                print(f"{foundTabs.index(foundTab) + 1}. {foundTab}")

        elif(len(foundTabs) == 1):
            print("Found one tab!!")
            print(foundTabs[0])

        else:
            print("Taby wasnt found!!")


    def help():
        """
        An help menu
        """
        print("wtTaby - Help menu!")
        print("To run: wtTaby [FUNCTION] [OPERATOR(If needed)]")
        print("Functions - ")
        print(" Setup - \n '--setup' : To setup the system, Add '-a' to auto search for the settings file\n")
        print(" New Tab - \n '--newTaby' : To add a new tab\n")
        print(" Show - \n '--show' : Shows the tabs that are in the settings.json file\n")
        print(" Set Default - \n '--default' : Sets a new default tab ")

