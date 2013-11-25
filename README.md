####   #  ####  #####    ####
#   #        #  #       #    #
####   #  ####  #  ###  #    #
#      #  #     #   ##  #    #
#      #  ####  #####    ####
==============================================
In car computer utilizing RPi

Daryl W. Bennett ~kd8bny@gmail.com
http://kd8bny.blogspot.com/


Requirements
==============================================
Software
- Python 2.7
- python-serial
- python-qt4
- blueman (Only to use BT features)
- pyqt4-dev-tools ~Optional for devs

Hardware
- RPi :P
- OBD2 Sensor (BT or USB)
- GPS ~Optional

Instructions
==============================================
1.) cd pi2go dir
2.) run 'make run'

dev
-----
- make clean        ~ Removes all temp files
- make build        ~ Rebuilds all dependencies 
- make initbuild    ~ Build UI for first time !!! USE MAKE BUILD after!!!

Changelog
==============================================
V1 R*
---------------
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
