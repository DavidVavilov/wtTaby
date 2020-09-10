#wtTaby - David Vavilov 2020
import os
import sys
import subprocess
import json
import configparser
from osFunctions import osFunctions
from tabyFunctions import tabyFunctions
 
def main():
    """
    The main function.
    Gets argv's from the command prompt
    """
    config = configparser.ConfigParser()
    config.read('config/config.ini')

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
            print("Path -",osFunctions.searchForSettings())
        
        if(function == "--edit"):
            if(len(sys.argv) > 2):
                tabName = sys.argv[2]
                tabyFunctions.editTaby(tabName)
        
        if(function == "--default"):
            tabyFunctions.setDefault()

        if(function == "--save"):
            tabyFunctions.saveTabs()

        if(function == "-v"):
            """
            Prints the version and when it was last updated
            Via the 'config.ini' file
            """
            WTTABY_VERSION = config['wtTaby']['version']
            WTTABY_LAST_DATE = config['wtTaby']['lastUpdate']
            print(f"wtTaby - version {WTTABY_VERSION}")
            print(f"Last Update - {WTTABY_LAST_DATE}")
    else:
        print("wtTaby")
        print("To run: wtTaby [FUNCTION] [OPERATOR(If needed)]")
        print("Functions - ")
        print(" Setup - \n '--setup' : To setup the system, Add '-a' to auto search for the settings file\n")
        print(" New Tab - \n '--newTaby' : To add a new tab\n")
        print(" Show - \n '--show' : Shows the tabs that are in the settings.json file\n")
        print(" Set Default - \n '--default' : Sets a new default tab ")
    



if __name__=="__main__":
    main()