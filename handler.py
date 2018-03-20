# this file is responsible for searching spotify for metadata
#this is not the final form!!!
import spotipy
import spotipy.util as util


def authRoutine():
    scope = " "
    username = input("Username: ")
    global token
    token = util.prompt_for_user_token(username,scope)

    if token:

        print("token",token)
    else:
        print("Can't get token for", username)

def metaFetch(song,artist):
    print("globalToken1",token)
    spInteract = spotipy.Spotify(auth=token)
    queryResults = spInteract.search(q='track:'+song+' artist:'+artist,type='track')
    print(queryResults)
