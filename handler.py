# this file is responsible for searching spotify for metadata
#this is not the final form!!!
import spotipy
import spotipy.util as util




def authRoutine():
    scope = " "
    username = input("Username: ")  #Ask the user for their username
    global token
    token = util.prompt_for_user_token(username,scope)

    if not token:
        print("Can't get token for", username)

def metaFetch(song,artist):
    spInteract = spotipy.Spotify(auth=token)
    queryResults = spInteract.search(q='track:'+song+' artist:'+artist,type='track')
    dataA = queryResults["tracks"]

    if dataA["total"]>0:
        #The following code goes from the full API result down to more and more specific entries in either a dict or list.
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
