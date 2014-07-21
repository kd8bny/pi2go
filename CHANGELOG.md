Changelog
==============================================
V1 R*
---------------
7-20-14
make - Added APscheduler. Remove .gz packages
*go - Cleaned import, Added scheduler for maintenance tasks [WIP!!!]

7-16-14
*OBD - MAJOR FIXES!!! Fixed all data grabs. Added engine runtime PID
*go -add OBD old values

6-21-14
*go - Fixed freezing UI during OBDII, Remove QWT plot- favored progress bars
make - temp removed makeQWT

------------------
*log - Fixed empty log issue and missing directory issue
*go -Searches work!!! Add new signal/slot style....ish. Maintenance log now updates when deleting 
make - Added support for new search box. Fixed update QWT issue
main - Changed layout a little. Working with a new idea for GPS

6-18-14
*OBD - prepping for diagnostics addition
*go - added a few more settings. A little pseudo code
Prepping for version 2!

6-16-14
main.* - Major UI cleanup. Removed car tab gimiky feature
*go - removed cartab back end testing graph stuff...can be ignored. Removed logGPS buttons
make - add pip

6-07-14
makefile - Fixed path error
*log - fixed path error with make. Fixed Bug when log doesnt exist
*go && *log - Added deleted last entry

6-06-14
Thinking about rolling V2 soon....Till all the features I have work that is
*go & *log - Added feature to read the last logged data
*go Fixed ATSP error
makeQWT is still funky for builds....working on that

----------------
TONS OF CODE FIXES. Squishing bugs galore :D
*go & *OBD - Added the option for metric or US units
    Also fixed the clear codes option
*go Fixed the settings radio button from not functioning (derp)

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
