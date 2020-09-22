#wtTaby - David Vavilov 2020
import os
import sys
import subprocess
import json
import configparser
import requests
from packaging import version
from osFunctions import osFunctions
from tabyFunctions import tabyFunctions
 
def main():
    """
    The main function.
    Gets argv's from the command prompt
    """
    currDir = os.getcwd()
    config = configparser.ConfigParser()
    config.read(f'{currDir}/config/config.ini')
    tabyFuncs = tabyFunctions()
    if(len(sys.argv) > 1):
        function = sys.argv[1]
        
        if(function == "--setup"):
            if(len(sys.argv) > 2 and sys.argv[2] == '-a'):
                tabyFuncs.autoSetup()
            else:
                tabyFuncs.setup()
        
        if(function == "--newTaby"):
            tabyFuncs.newTaby()
        
        if(function == "--help"):
            tabyFuncs.help()
        
        if(function == "--show"):
            tabyFuncs.printTabs()
        
        if(function == "--search"):
            print("Path -",osFunctions.searchForSettings())
        
        if(function == "--edit"):
            if(len(sys.argv) > 2):
                tabName = sys.argv[2]
                tabyFuncs.editTaby(tabName)
        
        if(function == "--delete"):
            if(len(sys.argv) > 2):
                tabName = sys.argv[2]
                tabyFuncs.deleteTab(tabName)
        
        if(function == "--default"):
            tabyFuncs.setDefault()

        if(function == "--save"):
            tabyFuncs.saveTabs()
        
        if(function == "--checkUp"):
            checkUpdate(config)

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
        print(" Edit a taby - \n '--edit [TABY NAME]', If name has couple words use - \"TABY NAME\"\n")
        print(" Show - \n '--show' : Shows the tabs that are in the settings.json file\n")
        print(" Set Default - \n '--default' : Sets a new default tab ")

    
def checkUpdate(currConfig):
    """
    A function that if updates are available for wtTaby
    Input : currConfig (The content from the local config file)
    """
    API_LINK = "https://api.github.com/repos/DavidVavilov/wtTaby/contents/src/config/config.ini"
    apiResponse = requests.get(API_LINK).json()
    CONFIG_URL = apiResponse['download_url']
    configFromGithub = configparser.ConfigParser()
    try:
        configResponse = requests.get(CONFIG_URL)
        configFromGithub.read_string(str(configResponse.text))
        versionFromGithub = configFromGithub['wtTaby']['version']
        localversion = currConfig['wtTaby']['version']
        if(version.parse(versionFromGithub) > version.parse(localversion)):
            print(f"Update available to wtTaby version - {versionFromGithub}")
        else:
            print(f"No update available, wtTaby Version - {localversion}")

    except Exception as e:
        print("Checking updates is unavailable, Try again later.")


if __name__=="__main__":
    main()
