#kd8bny Makefile
#Project: pi2go
#V1 R3
     
# Cleans your directory
clean:
	@ echo "*** Removing all temp files ***"
	@ rm -f *.pyc
	@ rm -f *.txt
	@ rm -f *~
	@ echo "*** Complete ***"

# Update 
update:
	@ make clean
	@ echo "*** Updating ***"
	@ git checkout *
	@ echo "*** Complete ***"

# Auto install required packages
prereq:
	@ echo "*** Installing Prerequisites... Standby ***"
	@ sudo apt-get install git python2.7 python-serial python-qt4 python-numpy python-qwt5-qt4 blueman pyqt4-dev-tools
	@ echo "*** Complete ***"

# Runs the code
run:
	sudo python2.7 pi2go.py

# Build UI for first time !!! USE MAKE BUILD after!!!
initbuild:
	#Build main UI
	@ echo "***Initial build__Utilizing pyuic4***"
	@ pyuic4 -xd -o main.py main.ui

# Rebuilds the interface
build:
	#Build main UI
	@ echo "*** Utilizing pyuic4 ***"
	@ rm main.py
	@ pyuic4 -xd -o main.py main.ui
