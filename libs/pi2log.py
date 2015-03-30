#pi2log
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a DIY in car computer using RPi

#R2

import sys, os, xlwt, xlrd

from tempfile import TemporaryFile
from xlwt import Workbook
from xlrd import open_workbook
from xlutils.copy import copy

import dropbox

class pi2log():

    def __init__(self):
        
        try:
           self.careBook = open_workbook('../logs/MaintainanceLog.xls', formatting_info=True)
           self.logSheet = self.careBook.sheet_by_index(0)

        except:
            if not os.path.exists('../logs'):
                os.makedirs('../logs')

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
        lastRow = self.logSheet.nrows
        if lastRow==1:
            careValues.insert(0, 'NA')
            careValues.insert(1, 'NA')
            careValues.insert(2, 'NA')
            careValues.insert(3, 'NA')
        else:
            careValues.insert(0, self.logSheet.cell(lastRow-1,0).value)
            careValues.insert(1, self.logSheet.cell(lastRow-1,1).value)
            careValues.insert(2, self.logSheet.cell(lastRow-1,2).value)
            careValues.insert(3, self.logSheet.cell(lastRow-1,3).value)
        
        return careValues

    def delLast(self):
        """Delete the last entry in log"""
        if self.logSheet.nrows != 0:
            tempBook = xlwt.Workbook()
            tempSheet = tempBook.add_sheet('Log')
            for rowNum in range(0, self.logSheet.nrows-1):
                for colNum in range(self.logSheet.ncols):
                    getValue = self.logSheet.cell(rowNum,colNum).value
                    tempSheet.write(rowNum,colNum,getValue)
                    tempSheet.col(3).width = 30000
                    tempBook.save('../logs/MaintainanceLog.xls')     
        return

    def search(self, task):
        """Lists on Lists on Lists"""
        taskList = []

        for rowNum in range(0, self.logSheet.nrows):
            if self.logSheet.cell(rowNum,1).value == task:
                taskList.append(self.logSheet.row_values(rowNum))

        return taskList

class pi2cloud(object):

    def __init__(self):
        pass

    def setup(self):
        # Get your app key and secret from the Dropbox developer website
        app_key = 's57exialypbu0eo'
        app_secret = 'bif2m6w2fu68h2ps'
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        print flow
        # Have the user sign in and authorize this token
        authorize_url = flow.start()
        print '1. Go to: ' + authorize_url
        print '2. Click "Allow" (you might have to log in first)'
        print '3. Copy the authorization code.'
        code = raw_input("Enter the authorization code here: ").strip()

        # This will fail if the user enters an invalid authorization code
        access_token, user_id = flow.finish(code)

        client = dropbox.client.DropboxClient(access_token)
        print 'linked account: ', client.account_info()
        return client

    def sync(self):
        client = self.setup()
        response = client.put_file('../logs/MaintainanceLog.xls', f)

if __name__ == "__main__":
    test = pi2cloud()
    test.sync()    
