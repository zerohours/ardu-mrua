import serial, time

class arduino_controler:

    def __init__(self):
        self.serial=serial.Serial('/dev/ttyACM0', 9600, timeout=None)

    def __getData(self):
	return self.serial.readline().replace("\r\n","")

    def __sendData(self, serial_data):
        while(self.__getData()!="wtf"):
	    pass
	self.serial.write(str(serial_data))
    
    def read_line(self):
	return self.serial.readline()

    def move_servo(self,grades):
	self.serial.__sendData(2)
	self.serial.__sendData(grades)

    def disconnect(self):
        self.serial.close()
	return True
