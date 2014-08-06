#pi2OBD ~interface between pi2go and the OBD sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a DIY in car computer using RPi

#R5

import serial, string, time
from PyQt4.QtCore import *
from main import *
import config

class pi2OBD(object):

    def __init__(self):
        try:
            self.default = config.config().loadSave()
            self.serialIO = serial.Serial(self.default['serialDevice'], 9600, timeout=None)
        except serial.SerialException:
            print "Serial Issue"
    
    def serialTX(self, cmd):
        """Sends cmd to OBD"""
        self.serialIO.flushInput()
        self.serialIO.flushOutput()
        self.serialIO.write("01 "+cmd+"\r")
        
        return

    def serialRX(self):
        """Reads and formats output from OBD"""
        serialList = self.serialIO.readline().split(' ')
        valueList = []
        for value in serialList:
            if value == '>01':
                return -1
            else:
                for char in value:
                    if char == '\r':
                        valueList.append(value[0:2])
                        return valueList[2:len(valueList)]
                valueList.append(value)

        return valueList[2:len(valueList)]
            
    def speed(self, oldOBD):
        """Grabs speed of vehicle"""
        self.serialTX("0D")
        speedValues = self.serialRX()
        if speedValues == -1:
            speed_float = oldOBD[0]
        else:
            speed_hex = speedValues[0]
            speed_float = float(int("0x"+speed_hex, 0))
        
            if config.units == 'metric':
                return speed_float
            else:
                speed_float = speed_float*0.621371
        
        return speed_float
    
    def rpm(self, oldOBD):
        """Grabs RPM of Engine"""
        self.serialTX("0C")
        rpmValues = self.serialRX()
        if rpmValues == -1:
            rpm_final = oldOBD[1]
        else:
            rpm_hex = rpmValues[0]
            rpmValues[0] = float(int("0x"+rpmValues[0], 0))
            rpmValues[1] = float(int("0x"+rpmValues[1], 0))
            
            rpm_final = ((rpmValues[0]*256)+rpmValues[1])*.25
        
        return rpm_final
        
    def intake_temp(self, oldOBD):
        """Grabs Intake Air temp (Temp outside)"""
        self.serialTX("0F")
        tempValues = self.serialRX()
        if tempValues == -1:
            temp_final = oldOBD[2]
        else:
            temp_hex = tempValues[0]
            temp_float = float(int("0x"+temp_hex, 0))
            
            if config.units == 'metric':  
                temp_final = temp_float-40 
            else: 
                temp_final = temp_float*(9/5)+32
        
        return temp_final       

    def coolant_temp(self, oldOBD):
        """Grabs Intake Air temp (Temp outside)"""
        self.serialIO.write("05")
        tempValues = self.serialRX()
        if tempValues == -1:
            temp_final = oldOBD[3]
        else:
            temp_hex = tempValues[0]
            temp_float = float(int("0x"+temp_hex, 0))
            
            if config.units == 'metric':  
                temp_final = temp_float-40 
            else: 
                temp_final = temp_float*(9/5)+32
        
        return temp_final 
        
    def load(self, oldOBD):
        """Grabs Total Engine Load"""
        self.serialIO.write("04")
        loadValues = self.serialRX()
        if loadValues == -1:
            temp_final = oldOBD[4]
        else:
            load_hex = loadValues[0]
            load_float = float(int("0x"+load_hex, 0))
            load_final = (load_float*100)/255

        return load_final
            
    def run_time(self, oldOBD):
        """Will grab amount of time engine has been running"""
        self.serialIO.write("1F")
        runValues = self.serialRX()
        if runValues == -1:
            run_final = oldOBD[5]
        else:
            runValues[0] = float(int("0x"+runValues[0], 0))
            runValues[1] = float(int("0x"+runValues[1], 0))
            run_final = ((runValues[0]*256)+runValues[1])

        return run_final

    def setup(self):
        """Set up OBD Comm"""
        self.serialIO.write("ATZ \r")
        time.sleep(2)
        self.serialIO.write("ATSP %d \r" % config.ATSP)
        time.sleep(.5)
        self.serialIO.readline().split(' ')
        self.serialIO.write("01 00 \r")
        time.sleep(.5)

        return
        
    def OBDread(self, OBDvalues):
        """Function to read and write data: [speed, rpm, intake, coolant, load, runtime]"""
        OBDvalues[0] = self.speed(OBDvalues)
        OBDvalues[1] = self.rpm(OBDvalues)
        OBDvalues[2] = self.intake_temp(OBDvalues)
        OBDvalues[3] = self.coolant_temp(OBDvalues)
        OBDvalues[4] = self.load(OBDvalues)
        OBDvalues[5] = self.run_time(OBDvalues)

        return OBDvalues  

class pi2diag(pi2OBD):

    def __init__(self):
        pi2OBD.__init__(self)

    def clearCodes(self):
        """Clear all trouble codes"""
        self.serialIO.write("04")
        return

    def clearCodes_time(self):#TODO
        #4E
        pass
        
if __name__ == "__main__":
    test = pi2OBD()
    #test.setup()
    OBDvalues = test.rpm([1])
    print OBDvalues
