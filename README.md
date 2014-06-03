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
- git
- Python 2.7
- python-serial
- python-qt4
- python-numpy
- python-qwt5-qt4 
- python-odf

Optional
- blueman (Only to use BT features)
- pyqt4-dev-tools ~Optional for devs

Hardware
- RPi :P
- OBD2 Sensor (BT or USB)
- GPS ~Optional

Instructions
==============================================
To Setup
	$ make prereq

To Run
	$ make run

To Update
	$ make update

For Dev
	$ make clean        ~ Removes all temp files
	$ make build        ~ Build UI and all dependencies 

Ideas/TODO
==============================================
- Better signals/sockets
- Better version tracking
- Data server
- OBD data tracking
- Options for USB or BT OBDII
- Switch to new signals
