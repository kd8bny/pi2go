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
           self.careBook = open_workbook('../logs/MaintainanceLog.xls', formatting_info=True)
           self.logSheet = self.careBook.sheet_by_index(0)

        except:
            self.careBook = xlwt.Workbook()
            self.logSheet = self.careBook.add_sheet('Log')
            self.format()
            self.careBook.save('../logs/MaintainanceLog.xls')

            self.careBook = open_workbook('../logs/MaintainanceLog.xls', formatting_info=True)
            self.logSheet = self.careBook.sheet_by_index(0)
            

    def format(self):
        """Set Data Headers: No existing log"""
        self.logSheet.write(0,0,'Date')
        self.logSheet.write(0,1,'Task')
        self.logSheet.write(0,2,'Odometer')
        self.logSheet.write(0,3,'Comments')
        self.logSheet.col(3).width = 30000

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
        tempBook.save('../logs/MaintainanceLog.xls')

        return

    def readLast(self):
        """Grab last recored data set"""
        careValues = []
        lastRow = self.logSheet.nrows-1
        if self.logSheet.cell(lastRow,0).value == 'Date':
            careValues.insert(0, 'NA')
            careValues.insert(1, 'NA')
            careValues.insert(2, 'NA')
            careValues.insert(3, 'NA')
        else:
            careValues.insert(0, self.logSheet.cell(lastRow,0).value)
            careValues.insert(1, self.logSheet.cell(lastRow,1).value)
            careValues.insert(2, self.logSheet.cell(lastRow,2).value)
            careValues.insert(3, self.logSheet.cell(lastRow,3).value)
        
        return careValues

    def delLast(self):
        """Delete the last entry in log"""
        tempBook = xlwt.Workbook()
        tempSheet = tempBook.add_sheet('Log')
        for rowNum in range(0, self.logSheet.nrows-1):
            for colNum in range(self.logSheet.ncols):
                getValue = self.logSheet.cell(rowNum,colNum).value
                tempSheet.write(rowNum,colNum,getValue)
        tempSheet.col(3).width = 30000
        tempBook.save('../logs/MaintainanceLog.xls')

        return



if __name__ == "__main__":
    test = pi2log()
    #test.addData(['test','test','test','test'])
    test.delLast()
    #better (row0)
    #row1 = self.logSheet.row(1)
    #row1.write(0,'A2')
    #row1.write(1,'B2')
