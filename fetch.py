# this file downloads the website and gets the song artist and track

import platform             #Used for OS detection
import os                   #Used for running commands in the system shell
import spotipy              #Used to interact with Spotify API

# wget website and extract song title/artist.
def getCurrentSong():

    # checks OS and uses appropriate delete tool
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system("rm 087.html")

    elif platform.system() == "Windows":
        os.system("del 087.html")

    else:
        print("bruv you on a leappad or some shit")

    # makes local copy of website
    os.system("wget --quiet muzakwpn.muzak.com/wpn/087.html")

    # this horrible mess picks out the important information
    # I am confident there is a more elegant way to do this...
    with open("087.html") as website:
        docLines = website.readlines()
        trackLine = docLines[15]
        trackToSplit = trackLine[50:]
        track = trackToSplit.split("<")
        currentTrack = track[0]
        currentTrack = currentTrack.split(", by ")
        currentSong = currentTrack[0]
        currentArtist = currentTrack[1]
        songInformation = currentSong, currentArtist
        return(songInformation)
