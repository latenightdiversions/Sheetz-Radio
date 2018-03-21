import fetch
import log
import handler
import time
import os
import platform

def main():
    # this is a test change to see how gpg signed commits work...
    # initial declarations and simple formatting
    log.appendLog()
    print("You will need to log in to Spotify to continue. Please follow any onscreen prompts.")
    handler.authRoutine()
    songInformationCurrent = fetch.getCurrentSong()
    songInformationOld = songInformationCurrent
    screenRefresh()
    print("Current song playing: ", songInformationCurrent[0], ", by", songInformationCurrent[1])
    print("Attempting to fetch track metadata from Spotify...")
    handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])

    # pretty much the main function loop
    while True:

        # gets tuple of song and artist in that order
        songInformationCurrent = fetch.getCurrentSong()

        # checks to see if song changed
        if songInformationCurrent != songInformationOld:
            log.appendLog()
            songInformationOld = songInformationCurrent
            screenRefresh()
            #print("Current song playing: ", songInformationCurrent[0], ", by", songInformationCurrent[1])
            handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])
        # pulls data from website every 5 seconds
        time.sleep(5)

def screenRefresh():
    #clear the command line screen using the appropriate command based on the user's operating system
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("wtf lol")


# I don't really understand why this works but it does
if __name__ == "__main__":
    main()
