#pi2OBD ~interface between pi2go and the OBD sensor
###################################################
#In car use of the raspberry pi OBD functions
#Daryl W. Bennett --kd8bny@gmail.com
#Purpose is to have a DIY in car computer using RPi

#V4 R0

import serial, string, time
from PyQt4.QtCore import *
from main import *
import config

class pi2OBD(object):

    def __init__(self):
        try:
            self.serialIO = serial.Serial(config.serialDevice, 38400, timeout=1)
        except:
            print "Serial Issue"
        
    def speed(self):
        """Grabs speed of vehicle"""
        self.serialIO.write("01 0D \r")
        speed_list = self.serialIO.readline().split(' ')
        speed_hex = speed_list[0][4:6]
        try:
            speed_float = float(int("0x"+speed_hex, 0))
        except:
            return 0
        
        if config.units == 'metric':
            speed_float = speed_float
        else:
            speed_float = speed_float*0.621371
        return speed_float
    
    def rpm(self):
        """Grabs RPM of Engine"""
        self.serialIO.write("01 0C \r")
        rpm_list = self.serialIO.readline().split(' ')
        rpm_value = []
        rpm_value.append(rpm_list[0][4:6])
        rpm_value.append(rpm_list[0][6:8])
        try:
            rpm_value[0] = float(int("0x"+rpm_value[0], 0))
            rpm_value[1] = float(int("0x"+rpm_value[1], 0))
        except:
            return 0
            
        #Calulate RPM
        rpm_final = ((rpm_value[0]*256)+rpm_value[1])*.25
        return rpm_final
        
    def intake_temp(self):
        """Grabs Intake Air temp (Temp outside)"""
        self.serialIO.write("01 0F \r")
        temp_list = self.serialIO.readline().split(' ')
        temp_hex = temp_list[0][4:6]
        try:
            temp_float = float(int("0x"+temp_hex, 0))
        except:
            return 0
        
        if config.units == 'metric':  
            temp_final = temp_float-40 
        else: 
            temp_final = temp_final*(9/5)+32
        return temp_final
        
    def coolant_temp(self):
        """Grabs Intake Air temp (Temp outside)"""
        self.serialIO.write("01 05 \r")
        temp_list = self.serialIO.readline().split(' ')
        temp_hex = temp_list[0][4:6]
        try:
            temp_float = float(int("0x"+temp_hex, 0))
        except:
            return 0
        
        if config.units == 'metric':   
            temp_final = temp_float-40
        else:
            temp_final = temp_final*(9/5)+32
        return temp_final
        
    def load(self):
        """Grabs Total Engine Load"""
        self.serialIO.write("01 04 \r")
        load_list = self.serialIO.readline().split(' ')
        load_hex = load_list[0][4:6]
        try:
            load_float = float(int("0x"+load_hex, 0))
        except:
            return 0
            
        load_final = (load_float*100)/255
        return load_final
        
    def run_time(self): #TODO
        """Will grab amount of time engine has been running"""
        self.serialIO.write("01 7F \r")
        temp_list = self.serialIO.readline().split(' ')
        pass

    def setup(self):
        """Set up OBD Comm"""
        self.serialIO.write("ATZ \r")
        time.sleep(2)
        self.serialIO.write("ATSP %d \r" % self.config.ATSP)
        time.sleep(.5)
        self.serialIO.readline().split(' ')
        self.serialIO.write("01 00 \r")
        time.sleep(.5)
        return
        
    def OBDread(self):
        """Function to read and write data: [speed, rpm, intake, coolant, load]"""
        OBDvalues = [0, 0, 0, 0, 0]
        OBDvalues[0] = self.speed()
        OBDvalues[1] = self.rpm()
        OBDvalues[2] = self.intake_temp()
        OBDvalues[3] = self.coolant_temp()
        OBDvalues[4] = self.load()

        return OBDvalues  

class pi2diag(pi2OBD):

    def __init__(self):
        pi2OBD.__init__(self)

    def clearCodes(self):
        """Clear all trouble codes"""
        self.serialIO.write("04")
        return
        
if __name__ == "__main__":
    test = pi2diag()
    test.clearCodes()
