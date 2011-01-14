import serial, time

class arduino_controlador:

    def __init__(self):
        self.serial=serial.Serial('/dev/ttyACM0', 9600, timeout=None)

    def __capturarData(self):
	return self.serial.readline().replace("\r\n","")

    def __enviarData(self, serial_data):
        while(self.capturarData()!="Que"):
	    pass
	self.serial.write(str(serial_data))
    
    def leer_linea(self):
	return self.serial.readline()

    def desconectar(self):
        self.serial.close()
	return True
