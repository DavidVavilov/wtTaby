#wtTaby David Vavilov 2020
import json
import requests
import configparser
from packaging import version

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
            print(f"No updates available, wtTaby Version - {localversion}")

    except Exception as e:
        print("Checking updates is unavailable, Try again later.")