import fetch
import log
import time
import os

def main():
    # this is a test change to see how gpg signed commits work...
    # initial declarations and simple formatting
    log.appendLog()
    songInformationCurrent = fetch.getSongData()
    songInformationOld = songInformationCurrent
    os.system("clear")
    print("Current song playing: ", songInformationCurrent[0], ", by", songInformationCurrent[1])

    # pretty much the main function loop
    while True:

        # gets tuple of song and artist in that order
        songInformationCurrent = fetch.getSongData()

        # checks to see if song changed
        if songInformationCurrent != songInformationOld:
            log.appendLog()
            songInformationOld = songInformationCurrent
            os.system("clear")
            print("Current song playing: ", songInformationCurrent[0], ", by", songInformationCurrent[1])

        # pulls data from website every 5 seconds
        time.sleep(5)

# I don't really understand why this works but it does
if __name__ == "__main__":
    main()
