import serial
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    print "Verifique que ARDUINO este conectado al computador"
else:
    comando = 'init'
    while comando == 'init':
        ser.write('4')
        print ser.readline()
        comando = raw_input("Desea seguir? ")
    print "adios ..."
    ser.close()
