#pi2log
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a DIY in car computer using RPi

#V1 R0

import sys, os, xlwt, xlrd
import config

from tempfile import TemporaryFile
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy


class pi2log():

    def __init__(self):
        
        try:
           self.careBook = open_workbook('MaintainanceLog.xls', formatting_info=True)
           self.logSheet = self.careBook.sheet_by_index(0)

        except:
            self.careBook = xlwt.Workbook()
            self.logSheet = self.careBook.add_sheet('Log')
            self.format()
            self.careBook.save('MaintainanceLog.xls')
            self.careBook.save(TemporaryFile())

    def format(self):
        """Set Data Headers: No existing log"""
        self.logSheet.write(0,0,'Date')
        self.logSheet.write(0,1,'Task')
        self.logSheet.write(0,2,'Odometer')
        self.logSheet.write(0,3,'Comments')
        self.logSheet.col(3).width = 30000

        #better (row0)
        #row1 = self.logSheet.row(1)
        #row1.write(0,'A2')
        #row1.write(1,'B2')
        return

    def addData(self, careValues):
        """Add row of data to the end of sheet"""
        tempBook = copy(self.careBook)
        tempSheet = tempBook.get_sheet(0)
        lastRow = self.logSheet.nrows 
        tempSheet.write(lastRow,0,careValues[0])
        tempSheet.write(lastRow,1,careValues[1])
        tempSheet.write(lastRow,2,careValues[2])
        tempSheet.write(lastRow,3,careValues[3])
        tempBook.save('MaintainanceLog.xls')
        return

if __name__ == "__main__":
    test = pi2log()
    test.addData(['test','test','test','test'])