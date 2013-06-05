####   #  ####  #####    ####
#   #        #  #       #    #
####   #  ####  #  ###  #    #
#      #  #     #   ##  #    #
#      #  ####  #####    ####
==============================================
In car computer utilizing RPi


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
6/4/13
*go R1 - Multithreading is now working. Also UI freeze bug is fixed. GPIO issues are fixed
*OBD R1 - Small bug fixes
main.ui R1 - Reorganized added missing features (Clear codes, new obd stats)

5/30/13
*ODB R1 - Added Air intake temp, Engine load, Engine coolant temp, clear codes, time on (in progress)
*go R1	- Added clear codes option (Not in GUI yet)

5/27/13
*ODB R1 - Serial IO now working. Soon to be integrated into GUI
