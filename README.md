his application is an audiobook player relying on command line VLC to 
play pre-collected list of mp3s. If this py made to autostart on RaspberryPi 
power on it takes the last played mp3 and continues playing from the beginning of that last mp3. 

How to use: 
This application relies to have a USB drive (FAT32 formatted) labeled as "BOOK". On that USB drive
it takes all mp3 files that are in the "MP3" folder. Within that folder file structure does not matter, 
I recommend to have each Audiobook in its own folder. 
Remove all special characters and spaces from the names of the folders and filenames (éáűőúöüó letters included). 

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