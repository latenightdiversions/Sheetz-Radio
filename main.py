# this is the main file

import fetch
import log
import handler
import time
import xFunctions

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
    xFunctions.screenRefresh()
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
            xFunctions.screenRefresh()
            handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])

        # refreshes current song from website every 5 seconds
        time.sleep(5)


# I don't really understand why this works but it does
if __name__ == "__main__":
    main()
