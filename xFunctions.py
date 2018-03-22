# file for assorted functions that don't seem to fit anywhere else

import os
import platform

def screenRefresh():

    #clear the command line screen using the appropriate command based on the user's operating system
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("bruv are u on a leappad")
