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

new_ardu = arduino_controlador()
time.sleep(15)
comando = raw_input("Que desea hacer? ")
if comando == 1:
    new_ardu.__enviarData(comando)
    tiempo = new_ardu.leer_linea()
    print "El tiempo es: "
    print tiempo
    while tiempo>=0:
        print new_ardu.leer_linea()
if comando == 0:
    new_ardu.desconectar()

