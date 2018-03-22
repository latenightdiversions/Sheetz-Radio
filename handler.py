# this file is responsible for searching spotify for metadata

import spotipy
import spotipy.util as util

"""NOTE: you need to set your Spotify API credentials as environment variables as of right now, this will be worked out in the future..."""
def authRoutine():

    # this part is essential, but who understands their own code less than those who write it?
    scope = " "

    # promps user to enter username, required to get user token from spotify
    username = input("Username: ")
    global token
    token = util.prompt_for_user_token(username,scope)

    # probably shouldn't happen but you never know
    if not token:
        print("Can't get token for", username)

# searches spotify for the current song, fetches metadata of song
def metaFetch(song,artist):

    # initiates connection with user token and makes query with the song name/artist
    spInteract = spotipy.Spotify(auth=token)
    queryResults = spInteract.search(q='track:'+song+' artist:'+artist,type='track')
    dataA = queryResults["tracks"]

    if dataA["total"]>0:

        #The following code goes from the full API result down to more and more specific entries in either a dict or list.
        # Don't question it
        dataB = dataA["items"]
        dataC = dataB[0]
        dataD = dataC["album"]
        dataE = dataD["images"]
        dataF = dataE[0]
        dataG = dataF["url"]            #ALBUM ART
        dataH = dataD["release_date"]   #RELEASE DATE
        dataI = dataC["popularity"]     #POPULARITY
        dataJ = dataC["duration_ms"]    #DURATION IN MILLISECONDS
        dataK = dataD["name"]           #ALBUM TITLE

        print("Track Data:\nTitle: ",song,"\nArtist: ",artist,"\nAlbum: ",dataK,"\nRelease Date: ",dataH,"\nPopularity: ",dataI,"\nSong Duration (ms): ",dataJ)
    else:
        print("No track data found in Spotify database.")
