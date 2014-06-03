#kd8bny Makefile
#Project: pi2go
#V1 R4
     
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
	@ git pull
	@ cd makeQWT/
	@ git pull makeQWT/
	@ echo "*** Complete ***"

# Auto install required packages
prereq:
	@ echo "*** Installing Prerequisites... Standby ***"
	@ sudo apt-get install git python2.7 python-serial python-qt4 python-numpy python-qwt5-qt4 blueman pyqt4-dev-tools python-xlwt python-xlrd 
	@ wget https://pypi.python.org/packages/source/x/xlutils/xlutils-1.7.1.tar.gz
	@ sudo pip install xlutils
	@ echo "*** Cloning makeQWT ***"
	@ git clone https://www.github.com/kd8bny/makeQWT.git
	@ echo "*** Complete ***"

# Runs the code
run:
	sudo python2.7 pi2go.py

# Build UI
build:
	#Build main UI
	@ echo "*** Utilizing pyuic4 ***"
	@ pyuic4 -xd -o main.py main.ui
	@ echo "*** Edit for QWT5 Support ***"
	@ sudo python2.7 makeQWT/makeQWT.py
	@ echo "*** Complete ***"
