# this file is responsible for searching spotify for metadata
#this is not the final form!!!
import spotipy
import spotipy.util as util
import json

def authRoutine():
    scope = " "
    #username = input("Username: ")
    username = "danfiscus"
    global token
    token = util.prompt_for_user_token(username,scope)

    if not token:
        print("Can't get token for", username)

def metaFetch(song,artist):
    spInteract = spotipy.Spotify(auth=token)
    queryResults = spInteract.search(q='track:'+song+' artist:'+artist,type='track')
    print(type(queryResults))
    print('popularity' in queryResults)
    print('duration_ms' in queryResults)
    print('explicit' in queryResults)
    print('available_markets' in queryResults)

'''

Album Art
Duration
Release Date
Popularity
SAMPLE output:::
{'tracks': {'href': 'https://api.spotify.com/v1/search?query=track%3APop+Lie+artist%3AOkkervil+River&type=track&market=US&offset=0&limit=10', 'items': [{'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/4iyJdf6kUi1QrnluWY0GfQ'}, 'href': 'https://api.spotify.com/v1/albums/4iyJdf6kUi1QrnluWY0GfQ', 'id': '4iyJdf6kUi1QrnluWY0GfQ', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/178284cc9fe07e4cb96fea14a5060460f097caaa', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/71c4cdba0cea978dbd53502e1923021d1bd476cc', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/363fd7a21fab3aef5a4f812eaf5a6192a0f465ec', 'width': 64}], 'name': 'The Stand Ins', 'release_date': '2008-09-09', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:4iyJdf6kUi1QrnluWY0GfQ'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 192306, 'explicit': False, 'external_ids': {'isrc': 'US38Y0812407'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/09QyUegQ8Hs4JrRb8JwB2r'}, 'href': 'https://api.spotify.com/v1/tracks/09QyUegQ8Hs4JrRb8JwB2r', 'id': '09QyUegQ8Hs4JrRb8JwB2r', 'name': 'Pop Lie', 'popularity': 25, 'preview_url': 'https://p.scdn.co/mp3-preview/627809cb62067e13455241892b7a9a8c7af13ea6?cid=eb0ad35c998b4968ade01f17a6c8ab56', 'track_number': 7, 'type': 'track', 'uri': 'spotify:track:09QyUegQ8Hs4JrRb8JwB2r'}, {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/5JgNGPzPrwa8gIWhSqeLmi'}, 'href': 'https://api.spotify.com/v1/albums/5JgNGPzPrwa8gIWhSqeLmi', 'id': '5JgNGPzPrwa8gIWhSqeLmi', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/71f5833205f426d53492856bafa6911b88cc1721', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/dd2378e21ef02a782404bd8be75d7d9e5a547971', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/547ce2234f39aa2ac3370da0d3eac169c70b4a9f', 'width': 64}], 'name': 'Pop Lie', 'release_date': '2009-04-21', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:5JgNGPzPrwa8gIWhSqeLmi'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 192306, 'explicit': False, 'external_ids': {'isrc': 'US38Y0914801'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/7aFhHZDQWSHq3EQjUN4yc3'}, 'href': 'https://api.spotify.com/v1/tracks/7aFhHZDQWSHq3EQjUN4yc3', 'id': '7aFhHZDQWSHq3EQjUN4yc3', 'name': 'Pop Lie', 'popularity': 4, 'preview_url': 'https://p.scdn.co/mp3-preview/fc4b59142082fa06fbdd0abb6d67db94b831d831?cid=eb0ad35c998b4968ade01f17a6c8ab56', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:7aFhHZDQWSHq3EQjUN4yc3'}, {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/5JgNGPzPrwa8gIWhSqeLmi'}, 'href': 'https://api.spotify.com/v1/albums/5JgNGPzPrwa8gIWhSqeLmi', 'id': '5JgNGPzPrwa8gIWhSqeLmi', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/71f5833205f426d53492856bafa6911b88cc1721', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/dd2378e21ef02a782404bd8be75d7d9e5a547971', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/547ce2234f39aa2ac3370da0d3eac169c70b4a9f', 'width': 64}], 'name': 'Pop Lie', 'release_date': '2009-04-21', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:5JgNGPzPrwa8gIWhSqeLmi'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5E7zSu46SqTmgKqsc0tFkY'}, 'href': 'https://api.spotify.com/v1/artists/5E7zSu46SqTmgKqsc0tFkY', 'id': '5E7zSu46SqTmgKqsc0tFkY', 'name': 'Okkervil River', 'type': 'artist', 'uri': 'spotify:artist:5E7zSu46SqTmgKqsc0tFkY'}], 'available_markets': ['AD', 'AR', 'AT', 'AU', 'BE', 'BG', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JP', 'LI', 'LT', 'LU', 'LV', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PT', 'PY', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 260399, 'explicit': False, 'external_ids': {'isrc': 'US38Y0914803'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/3fclaAxUh9mnKpXt6MihBV'}, 'href': 'https://api.spotify.com/v1/tracks/3fclaAxUh9mnKpXt6MihBV', 'id': '3fclaAxUh9mnKpXt6MihBV', 'name': 'Pop Lie - One Man Band Version', 'popularity': 3, 'preview_url': 'https://p.scdn.co/mp3-preview/076bd7112d9bdc8cf3eaab3a63415cbd9b08485a?cid=eb0ad35c998b4968ade01f17a6c8ab56', 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:3fclaAxUh9mnKpXt6MihBV'}], 'limit': 10, 'next': None, 'offset': 0, 'previous': None, 'total': 3}}







Attempting to fetch track metadata from Spotify...
Traceback (most recent call last):
  File "main.py", line 38, in <module>
    main()
  File "main.py", line 18, in main
    handler.metaFetch(songInformationCurrent[0],songInformationCurrent[1])
  File "D:\Programming\Python\Sheetz-Radio\handler.py", line 19, in metaFetch
    dictionaryThingy = json.loads(queryResults)
  File "C:\Program Files (x86)\Python36-32\lib\json\__init__.py", line 348, in loads
    'not {!r}'.format(s.__class__.__name__))
TypeError: the JSON object must be str, bytes or bytearray, not 'dict'


'''
