Changelog
==============================================
V1 R*
---------------
6-03-14
*go -  added feature for maintenance logs
*log - created Now saves data to spreadsheet

---------------
OBD&go - clean coade and add support for config
config - added again
main - added dev option for connection

6-01-14
*OBD - Reworked completely 
config - removed
*go - handles all signals. OBD is once again working. THANK GOD!!!
README - Update ideas. Removed thread handling and make fixes already complete

5-22-14
Removed Global variables and added config
*OBD - derp derp derp derp rework threads

5-9-14
make - Upped Revision. Removed initbuild option. Added makeQWT support to automatically build a working main.ui file. See http://www.github.com/kd8bny/makeQWT
1/5/13
*go - Working clock, Radio serial device selector
*OBD - Radio serial device selector
main - radio buttons

1/1/14
Mostly to push the new year.....Didnt like my Qt socket for OBD
*go - Changed the OBD socket handle, GPS buttons
main - Revised and cleaned again. Made room for OBD graph. Single stop/start button now. Same with GPS
		Added selector for BT or USB OBD2 (Not in *go atm)
make - Added auto install for required packages

12/31/13
MAJOR CHANGES TO UPDATES !!!!!WIP!!!! I have no way to test functions atm
make - Added the ability update from repo. See README, Updated for new temp data
*GPS - [WIP] Need to have device now. Fixed my plenty of object errors
*OBD - Needs testing before cleanup, Adding a temp file to store data. New feature - Graph data
		Upped revision.
*go  - Major changes to the OBD update
main - Layout cleanup

12/30/13
*OBD - Typos, Better signal/slot handling, process events handling(through thread)
*go - Better signal/slot handling.

11/24/13
main.* - Added GPS tabs
*2go - QT Fixes. Added GPS tab/functions. 
*2OBD - QT Fixes

11/23/13
Wow its been awhile.......
*all - Started GPS functions
*2GPS - added
*2go - Upped revision. Trying to depreciate guithread class
*2OBD - Upped revision. Handles own thread
*guiThread - Depreciated classes handle threads

8/23/13
*2go - Added ATSP function. Add settings function. Add blueman function
*2OBD - Added ATSP function. Add setup function
guiThread - Added first run setup call to *2OBD
main.ui - Added ATSP spinbox. Changed BT setup (See Requirments and )

7/9/13
MAJOR UPDATE!!!!!
*all - Upped revision numbers. Cleaned code!!
*2go - Updated Qthread handle. Now updates UI again. 
*2OBD - Added exceptions for invalid int. This will now let the program continue when serial has not yet  connected
guiThread - R2 Fixed major issues in how UI updates and threads are handled. Changed update time from 5s to 1s 
main.ui R3A - Added BT features NOT INCLUDED IN CODE (yet)

6/18/13
*go R2 - Now utilizes the new Qthread. ~Qthread read below
guiThread R1 - Added ~Should fix the GUI freezing while waiting for QT to process events

6/4/13
sOff R0 - New thread that allows the RPi to shutdown when vehicle losses key_on power. With this the RPi will not come to and abrubt halt losing integrity (Not in pi2go yet)
*go R1 - Multithreading is now working. Also UI freeze bug is fixed. GPIO issues are fixed
*OBD R1 - Small bug fixes
main.ui R1 - Reorganized added missing features (Clear codes, new obd stats)

5/30/13
*ODB R1 - Added Air intake temp, Engine load, Engine coolant temp, clear codes, time on (in progress)
*go R1	- Added clear codes option (Not in GUI yet)

5/27/13
*ODB R1 - Serial IO now working. Soon to be integrated into GUI