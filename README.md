####   #  ####  #####    ####
#   #        #  #       #    #
####   #  ####  #  ###  #    #
#      #  #     #   ##  #    #
#      #  ####  #####    ####
==============================================
In car computer utilizing RPi

Daryl W. Bennett ~kd8bny@gmail.com
http://kd8bny.blogspot.com/


Requirments
==============================================
- pyserial
- Python 2.x
- QT4

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
