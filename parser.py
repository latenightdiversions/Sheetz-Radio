import os

os.system("rm 087.html")
os.system("wget muzakwpn.muzak.com/wpn/087.html")
with open("087.html") as website:
    docLines = website.readlines()
    trackLine = docLines[15]
    trackToSplit = trackLine[50:]
    track = trackToSplit.split("<")
    currentTrack = track[0]
    currentTrack = currentTrack.split(", by ")
    currentSong = currentTrack[0]
    currentArtist = currentTrack[1]

'''
os.system("clear")
os.system("cls")
print("Song: ", currentSong)
print("Artist: ", currentArtist)
'''
