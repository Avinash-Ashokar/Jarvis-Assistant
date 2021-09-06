import os
from text_to_speech import *


def start(command):
    if 'pycharm' in command:
        text("Opening Pycharm")
        source = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"  # Enter the
        # correct Path according to your system
        os.startfile(source)

    elif 'resolve' in command:
        text("Opening Epic Games")
        path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Resolve.exe"  # Enter the correct Path
        # according to your system
        os.startfile(path)

    elif 'code' in command:
        text('Opening Visual Studio Code')
        path = "C:\\Users\\avina\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'games' in command:
        text('Opening Epic Games')
        path = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(path)

    elif 'Firefox' in command:
        text('Opening Firefox')
        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(path)