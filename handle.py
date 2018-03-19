# this file is responsible for searching spotify for metadata
#this is not the final form!!!

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


'''
export SPOTIPY_CLIENT_ID='eb0ad35c998b4968ade01f17a6c8ab56'
export SPOTIPY_CLIENT_SECRET='2cea7012b2fa41dca9264e9ca8353d64'
export SPOTIPY_REDIRECT_URI='http://localhost/'

http://spotipy.readthedocs.io/en/latest/#spotipy.oauth2.SpotifyClientCredentials
'''
