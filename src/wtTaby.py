#wtTaby - David Vavilov 2020
import os
import sys
import subprocess
import json
from osFunctions import osFunctions
from tabyFunctions import tabyFunctions


def main():
    #path = """C:/Users/Home/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"""
    if(len(sys.argv) > 1):
        function = sys.argv[1]
        
        if(function == "--setup"):
            if(len(sys.argv) > 2 and sys.argv[2] == '-a'):
                tabyFunctions.autoSetup()
            else:
                tabyFunctions.setup()
        
        if(function == "--newTaby"):
            tabyFunctions.newTaby()
        
        if(function == "--help"):
            tabyFunctions.help()
        
        if(function == "--show"):
            tabyFunctions.printTabs()
        
        if(function == "--search"):
            osFunctions.searchForSettings()
        
        if(function == "--default"):
            tabyFunctions.setDefault()

        if(function == "--save"):
            tabyFunctions.saveTabs()
    else:
        print("wtTaby")
        print("To run: wtTaby [FUNCTION] [OPERATOR(If needed)]")
        print("Functions - ")
        print("Setup - \n '--setup' : To setup the system, Add '-a' to auto search for the settings file")
        print("New Tab - \n '--newTaby' : To add a new tab")
        print("Show - \n '--show' : Shows the tabs that are in the settings.json file")
        print("Set Default - '--default'")
    



if __name__=="__main__":
    main()