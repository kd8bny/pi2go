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

Optional
- blueman (Only to use BT features)
- pyqt4-dev-tools ~Optional for devs

Hardware
- RPi :P
- OBD2 Sensor (BT or USB)
- GPS ~Optional

Instructions
==============================================
To Run
	$ make run

To Update
	$ make update

For Dev
	$ make clean        ~ Removes all temp files
	$ make build        ~ Rebuilds all dependencies 
	$ make initbuild    ~ Build UI for first time !!! USE MAKE BUILD after!!!

Ideas/TODO
==============================================
- Better signals/sockets
- Thread handler
- Better version tracking
- Data server
- OBD data tracking
- make autoinstall required package
- Options for USB or BT OBDII