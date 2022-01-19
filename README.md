# CABP
### Careless-AudioBookPlayer

## 1.Plot
My grandmother (92) lying in a retirement home is really in a bad shape. She stares at the ceiling all day long, only able to sit up with assistance. She cannot use a radio or handle a TV remote (or lost interest, which is even worse). 
I decided to build an AudioBook player that is so simple it has no controls and runs on a Raspberry Pi. The whole setup has a power socket. When it is plugged in Book continues from where it was left off, when unplugged stops. 

## 2.About CABP.py
This application is an audiobook player relying on command line VLC to play pre-collected list of mp3 files. If this py made to autostart on RaspberryPi power on it takes the last played mp3 and continues playing from the beginning of that last mp3. 

### How to use: 
This application relies to have a USB drive (FAT32 formatted) labeled as "BOOK". On that USB drive it takes all mp3 files that are in the "MP3" folder. Within that folder file structure does not matter, I recommend to have each Audiobook in its own folder. **Remove all special characters and spaces from the names of the folders and filenames (éáűőúöüó letters included). *

When the application started for the first time it looks for a playlist file (playlist.mcz) if it does not find it, creates it. At this point it makes sense to take a look into the created list file, to manually make sure file orders - within folders - was got right. 

After finishing playing of one file, listfile's first row deleted and playing continues with the next one. And this loop continues for eternety.  ..or when power shut off. 
Then on next reboot, filelist creation skipped and the first playlist item is played from the beginning. 

Application keeps a spare playlist file (original) to make it easier to set the player back to a previous state. There is a logfile that keeps track of startup times and file starting events. 

For further information, please read the READ.ME or contact czibere.a@gmail.com

## 3. Technical details
### 3.1 Removing special characters
To remove special characters I have used Antrenamer2. With this tool I was able to replace spaces with underscores and replace áéíóüö characters, so python can handle the paths. 

![Suitcase](/resources/Renaming_scheme.png)
## 4. Implementation (bringing to life)
This setup needs to be easy to use and compact, so I have looked up an extension power cord and an old PC loudspeaker with 3.5 mm jack and put them into an old suitcase. 
![Suitcase](/resources/suitcase01.jpg)

But as I said grandmother only able to sit up with assistance, some fellow old lady robes her blind. She takes away food from her table, etc. So some "access protection" is applied on the Audiobook player setup. 
![Suitcase](/resources/suitcase02.jpg)
## 5. Possible updates

Best regards, 
Attila Czibere
2022-01-04
