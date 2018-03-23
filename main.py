# this is the main file
# ^yeah no shit thanks

import fetch        #Gets update metadata
import log          #Generates CSV file
import handler      #Used to interact with Spotify API
import time         #Used for time machine purposes
import xFunctions   #Extra uncategorized functions
import argparse     #For detecting command-line arguments
import globals      #Storage for program-wide global variables


def main():

    # Dan is a sexy potato
    parser = argparse.ArgumentParser(description="I don't know what the text in this flag does.")               #Presumably, does something important
    parser.add_argument('--mode',help='Use \'debug\'. Enables extremely verbose output. May cause the gay.')    #Detects --mode argument
    parser.add_argument('--previews', help='Use \'on\'. Plays 30 second song previews in VLC if VLC is installed properly and not feeling particularly retarded.')
    args = parser.parse_args()

    if args.mode == 'debug':
        doDebugShit = True
    else:
        doDebugShit = False

    if args.previews == 'on':
        enablePreview = True
    else:
        enablePreview = False

    if doDebugShit:
        print('doing debug shit.')


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
