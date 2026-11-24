# Editor Companion

1. Application runs in real time and must be synced with a folder which is changing - sync time need not be shorter than 1 minute per sync - or could be trigger by a keybinding or update to the folder system

2. Aim is for software to track the length of time being taken to edit audio files and display the results - displaying method need not  be considered initially - a styled text / terminal (or command line for windows I guess) output will be fine to begin

3. During this tracking, the data of the file will need to be read to obtain the length - the data I would like to display is not how many files per minute are edited by how many seconds of audio are saved - as in, a file is taken into audition, edited there, then saved back to the same folderspace with the same name. So this resulting file, will have the newest modified date in the folder, and will be a shorter length than it was originally. The program will then take the file from the folderspace which was most recently modified, check the length of audio, and compare that with some kind of clock which is keeping count to calculate an average 

4. Very importantly is that program cannot touch any files in a way which could in any world allow them to be deleted or negatively modified since this is on a work machine.