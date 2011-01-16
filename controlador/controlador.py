#!/usr/bin/env python

import serial, time

class Controlador:

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
	print "Se estan ingresando a la opcion de servo\n"
	self.serial.write('2')
	print "Se estan ingresando los grados\n"
	self.serial.write(grades)

    def make_test(self):
	self.serial.write('1')
	time = 0
	while time != 0:
		time = self.serial.read()
	return time

    def disconnect(self):
        self.serial.close()
	return True
