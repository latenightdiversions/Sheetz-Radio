import fetch
import log
import handler
import time
import os
import platform

def main():

    log.appendLog()

    # initial declarations and simple formatting
    print("You will need to log in to Spotify to continue. Please follow any onscreen prompts.")

    # gets user token
    handler.authRoutine()

    # parses musak for song information
    songInformationCurrent = fetch.getCurrentSong()

    # initial declaration, enables detection of song changing
    songInformationOld = songInformationCurrent
    screenRefresh()
    print("Current song playing: ", songInformationCurrent[0], ", by", songInformationCurrent[1])
    print("Attempting to fetch track metadata from Spotify...")

    # feeds data from getCurrentSong() into a spotify query
    handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])

    # main function loop
    while True:

        # gets tuple of song and artist in that order
        songInformationCurrent = fetch.getCurrentSong()

        # checks to see if song changed
        if songInformationCurrent != songInformationOld:
            log.appendLog()
            songInformationOld = songInformationCurrent
            screenRefresh()
            handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])

        # refreshes current song from website every 5 seconds
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
