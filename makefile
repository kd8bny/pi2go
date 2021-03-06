#kd8bny Makefile
#Project: pi2go
#V1 R5

     
# Cleans your directory
clean:
	@ echo "*** Removing all temp files ***"
	@ rm -f libs/*.pyc
	@ rm -f libs/*.txt
	@ rm -f libs/*~
	@ rm -f *.gz
	@ echo "*** Complete ***"

# Update 
update:
	@ make clean
	@ echo "*** Updating ***"
	@ git pull
	@ cd makeQWT/ && git pull
	@ echo "*** Complete ***"

# Auto install required packages
prereq:
	@ echo "*** Installing Prerequisites... Standby ***"
	@ sudo apt-get install git python2.7 python-pip\
		python-serial python-numpy python-xlwt python-xlrd\
		python-qt4 pyqt4-dev-tools python-qwt5-qt4\
		blueman
	@ wget https://pypi.python.org/packages/source/x/xlutils/xlutils-1.7.1.tar.gz
	@ sudo pip install xlutils #apscheduler dropbox
	@ echo "*** Cloning makeQWT ***"
	@ git clone https://www.github.com/kd8bny/makeQWT.git
	@ echo "*** Complete ***"

# Runs the code
run:
	@ cd libs/ && sudo python2.7 pi2go.py

# Build UI
build:
	#Build main UI
	@ echo "*** Utilizing pyuic4 ***"
	@ pyuic4 -xd -o libs/main.py libs/main.ui
	@ pyuic4 -xd -o libs/search.py libs/search.ui
	@ pyuic4 -xd -o libs/error.py libs/error.ui
	@ echo "*** Edit for QWT5 Support ***"
	@ cd makeQWT/ && sudo python2.7 makeQWT.py
	@ echo "*** Complete ***"
