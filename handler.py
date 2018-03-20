# this file is responsible for searching spotify for metadata
#this is not the final form!!!
import spotipy
import spotipy.util as util

globalToken = ""

def authRoutine():
    scope = " "
    username = input("Username: ")
    token = util.prompt_for_user_token(username,scope)

    if token:
        globalToken = token
        print("token",token)
        print("globalToken",globalToken)
    else:
        print("Can't get token for", username)

def metaFetch(artist,song):
    spInteract = spotipy.Spotify()
    queryResults = spInteract.search(q='track:'+song+' artist:'+artist,type='track')
    print(queryResults)
