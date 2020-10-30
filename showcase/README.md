![logo](https://raw.githubusercontent.com/DavidVavilov/wtTaby/master/img/logo.png)

### About
wtTaby is a CLI for editing the tabs in the Microsoft Windows Terminal

Examples - 
- Note -  At this current stage to run wtTaby - python wtTaby.py [FUNCTION] [OPERATOR(If needed)]

```
>wtTaby
wtTaby
To run: wtTaby [FUNCTION] [OPERATOR(If needed)]
Functions -
 Setup -
 '--setup' : To setup the system, Add '-a' to auto search for the settings file

 New Tab -
 '--newTaby' : To add a new tab

 Edit a taby -
 '--edit [TABY NAME]', If name has couple words use - "TABY NAME"

 Show -
 '--show' : Shows the tabs that are in the settings.json file

 Set Default -
 '--default' : Sets a new default tab
```
- Option to show the tabs - 
```
>wtTaby --show
Windows Terminal Tabs -
GUID - {61c54bbd-c2c6-5271-96e7-009a87ff44bf}
Tab Name - This is a new name
---------------------------
GUID - {0caa0dad-35be-5f56-a8ff-afceeeaa6101}
Tab Name - Command Prompt
---------------------------
GUID - {a2838337-8e85-42c7-9813-d852452e90d7}
Tab Name - Ubuntu
---------------------------
GUID - {2c4de342-38b7-51cf-b940-2309a097f518}
Tab Name - Ubuntu 2020
---------------------------
GUID - {b453ae62-4e3d-5e58-b989-0a998ec441b8}
Tab Name - Azure Cloud Shell
---------------------------
```
- To create a new tab 
```
>wtTaby --newTaby
GUID generated - {0116779e-e522-4834-b575-a9e4764f887d}
Enter tab name: My new tab
Enter a commandline: cmd.exe
My new tab Taby Added to the Windows Terminal!
```

- To edit a tab (wtTaby --edit [TAB_NAME])
```
>wtTaby --edit "My new tab"
Found one tab!!
{'GUID': '{0116779e-e522-4834-b575-a9e4764f887d}', 'tabName': 'My new tab'}
Current settings -
    Name - My new tab
    Commandline - cmd.exe
Choose a key to edit - [name, commandline], Enter 'q' to exit: name
Enter a value for name: My new tab 2
Name was edited to My new tab 2
Choose a key to edit - [name, commandline], Enter 'q' to exit: q
Quiting edit tab....
```
And more coming soon....

**David Vavilov 2020**
