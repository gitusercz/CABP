#!/usr/bin/env python 
#

'''
This application is an audiobook player relying on command line VLC to 
play pre-collected list of mp3s. If this py made to autostart on RaspberryPi 
power on it takes the last played mp3 and continues playing from the beginning of that last mp3. 

How to use: 
This application relies to have a USB drive (FAT32 formatted) labeled as "BOOK". On that USB drive
it takes all mp3 files that are in the "MP3" folder. Within that folder file structure does not matter, 
I recommend to have each Audiobook in its own folder. 
Remove all special characters and spaces from the names of the folders and filenames.

When the application started for the first time it looks for a playlist file (playlist.mcz) if it does not 
find it, creates it. At this point it makes sense to take a look into the created list file, to manually make sure
file orders - within folders - was got right. 

After finishing playing of one file, listfile's first row deleted and playing continues with the next one. 
And this loop continues for eternety.  ..or when power shut off. 

Then on next reboot, filelist creation skipped and the first playlist item is played from the beginning. 

Application keeps a spare playlist file (original) to make it easier to set the player back to a previous state. 
There is a logfile that keeps track of startup times and file starting events. 

For further information, please read the READ.ME or contact czibere.a@gmail.com

Best regards, 
Attila Czibere
2022-01-04

'''

from datetime import datetime
from time import strftime
import datetime, commands, re
import time, os.path
import os

# Constants
button_delay = 1.0		# needed for debouncing and spawning a lot of os.system calls.
list_pointer = 0
cmd = ""				# command to be executed

# Path definitions
mp3folder = "/media/pi/BOOK/MP3"
mp3list = "/media/pi/BOOK/MP3/playlist.mcz"
mp3list_orig = "/media/pi/BOOK/MP3/playlist_orig.mcz"
logfile_path = "/media/pi/BOOK/logfile.txt"

print("\n\n AudioPlayer started!")
with open(logfile_path,"a") as logfile:
	logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",AudioPlayer started!\n")

if (not(os.path.exists(mp3list))):
	list_of_files = []
	for root, dirs, files in os.walk(mp3folder):
	    files.sort()
	    for file in files:
		if file.endswith(".mp3"):
		     #print(os.path.join(root, file))
		     list_of_files.append(os.path.join(root, file))
	with open(logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",USB drive seems to be brand new. Building new playlist file for listen tracking, and another for spare.\n")

	file = open(mp3list, "w")
	for element in list_of_files:
		file.write(element + "\n")
	file.close()
	print("\n\nFile written: \n" + mp3list)
	file = open(mp3list_orig, "w")
	for element in list_of_files:
		file.write(element + "\n")
	file.close()
	print("\n\nFile written: \n" + mp3list_orig)
	with open(logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Listfiles are created\n")

lines = open(mp3list, 'r').readlines()

while True: 
	with open(logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Attempting to play: " + lines[0])
	os.system("nvlc --play-and-exit " + lines[0])
	with open(logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Playing finished\n")
	lines.pop(0)
	file = open(mp3list, "w")
	for element in lines:
		file.write(element)
	file.close()
	with open(logfile_path,"a") as logfile:
		logfile.write(strftime("%Y-%m-%d %H:%M:%S")+",Currently played list entry removed\n")






