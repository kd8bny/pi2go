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
5/30/13
*ODB R1 - Added Air intake temp, Engine load, Engine coolant temp, clear codes, time on (in progress)
*go R1	- Added clear codes option (Not in GUI yet)

5/27/13
*ODB R1 - Serial IO now working. Soon to be integrated into GUI
