# CABP
### Careless-AudioBookPlayer

## 1.Plot
My grandmother (92) lying in a retirement home is really in a bad shape. She stares at the ceiling all day long, only able to sit up with assistance. She cannot use a radio or handle a TV remote (or lost interest, which is even worse). 
I decided to build an AudioBook player that is so simple it has no controls and runs on a Raspberry Pi. The whole setup has a switchable power socket. When it is plugged in Book continues from where it was left off, when unplugged stops. 

## 2.About CABP.py
This application is an audiobook player relying on command line mpg123 to play pre-collected list of mp3 files. This python script made to autostart on RaspberryPi power on it takes the last played mp3 and continues playing from the beginning of that last mp3. 

### How to use: 
Pre-copied mp3 files are picked up from "/home/pi/Music/MP3". Within that folder file structure does not matter, I recommend to have each Audiobook in its own folder. 

**Remove all special characters and spaces from the names of the folders and filenames (éáűőúöüó letters included).**

When the application started for the first time it looks for a playlist file ("/home/pi/Music/MP3/playlist.mcz") if it does not find it, creates it. At this point it makes sense to take a look into the created list file, to manually make sure file orders - within folders - was got right. "/home/pi/Music/MP3/playlist_orig.mcz" also gets created and untouched. If you want to reset the player and get it back to its initial state, you can either copy contents from this file to restore the original list or delete the mcz files so they recreated on next power-up. 

After finishing playing one file, listfile's first row deleted and playing continues with the next one. And this loop continues for eternety.  ..or when power shuts off. 
Then on next reboot, filelist creation skipped and the first playlist item is played from the beginning. 

There is a logfile that keeps track of startup times and file starting events. 

## 3. Technical details
### 3.1 Removing special characters
To remove special characters I have used Antrenamer2. With this tool I was able to replace spaces with underscores and replace áéíóüö characters, so python can handle the paths. 

![Suitcase](/resources/Renaming_scheme.png)
### 3.2 Choosing the playing tool
I have used [mpg123](https://www.mpg123.de/index.shtml) for other projets, so I was familiar with it already. It is a versatile tool and even has an [audiobook reading feature!](https://unix.stackexchange.com/questions/37018/command-line-audio-with-mpg123-how-to-save-position-in-audio-and-begin-from-th) I could not use it though, as it relies on keyboard buttonpresses. Also at that point I wanted to create this player to continue playback from the **exact** same time location minus 30 seconds where it was left off. mpg123 is able to seek to a certain frame not seconds. VLC can seek though. 

So I went on with nvlc and even created the script. It was working fine when started manually, but for some reason when the python script was supposed to be started as a service after boot-up it did not start. I did not spend time anymore on debugging switched back to the mpg123 solution and let go of the time-seeking feature. In the end I think it gives an even better user experience to begin with the last interrupted chapter. 

## 4. Implementation (bringing to life)
This setup needs to be easy to use and compact, so I have looked up an extension power cord and an old PC loudspeaker with 3.5 mm jack and put them into an old suitcase. 
![Suitcase](/resources/suitcase01.jpg)

But as I said grandmother only able to sit up with assistance, some fellow old lady robes her blind. She takes away food from her table, etc. So some "access protection" is applied on the Audiobook player setup. 
![Suitcase](/resources/suitcase02.jpg)

## 5. Possible updates
### 5.1 Running from an USB stick
There were another "feature letting go" moment during creation. Initially the logfiles, mcz playlists and the MP3 files were supposed to sit on a FAT32 formatted USB drive in the MP3 folder. The files were located in the "media\BOOK\MP3" folder if the USB drive is labelled "BOOK". This solution works 99% of the time. But as it turned out if you do not properly dismount the USB drive, next bootup it might show up in the folder "media\BOOK1\MP3". Then as "media\BOOK3\MP3" and so on. I never reached numberings higher than BOOK1, but I experienced this symptom too. CABP.py has this issue figured out, but to make the application safer to use, I decided to give up on using the USB drive and move all the books to the SD card. 

### 5.2 Real continuous playback
With multithread solution it could be tracked how along playing the current mp3 is. Then on next bootup nvlc could seek there. It is left to be figured out how to make nvlc start after boot. 


Best regards, 
Attila Czibere
2022-01-04
