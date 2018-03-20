import fetch
import csv
import os.path
from time import localtime, strftime

# Check if file exists, if not then declare the first row as an identifying row
if os.path.exists("history.csv") == False:
    with open('history.csv', 'a') as csvfile:
        logger = csv.writer(csvfile, dialect='excel')
        parameters = "Timestamp", "Song", "Artist"
        logger.writerow(parameters)

# appends song information to logfile
def appendLog():

    timeString = strftime("%Y-%m-%d %H:%M:%S", localtime())         #creates the string containing the date and time
    songInformation = fetch.getCurrentSong()                          #fetches the current song data
    parameters = timeString, songInformation[0], songInformation[1]


    with open('history.csv', 'a') as csvfile:           #open the log file as csvfile
        logger = csv.writer(csvfile, dialect='excel')   #create/open the log buffer as logger
        logger.writerow(parameters)                     #log relevant data to file
