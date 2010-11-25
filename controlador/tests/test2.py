#importando librerias
import sys
sys.path.append('../arduino')
from arduino import Arduino
from datetime import datetime
import time

#specify the port as an argument
my_board = Arduino('/dev/ttyUSB0')

#declare output pins as a list/tuple
my_board.output([9,13])

sensorPin=0
ledPin=9
sensorValue=0
sensorMin=1023
sensorMax=0
my_board.setHigh(13)
i=0
while(i<5):
    sensorValue = my_board.analogRead(sensorPin)
    sensorValue=int(sensorValue)
    if (sensorValue > sensorMax):
        sensorMax = sensorValue
    if(sensorValue<sensorMin):
	sensorMin=sensorValue    
    time.sleep(1)
    i+=1
    print sensorValue
my_board.setLow(13)
print sensorMin
print sensorMax
true=1
offed=0
tstart=0
tend=0
j=0
while(j<10):
  sensorValue = my_board.analogRead(sensorPin)
  sensorValue=int(sensorValue)
  if sensorValue>90:
      if offed==1:
          tend=datetime.now()
      my_board.setHigh(ledPin)
  else:
      if offed==0:
          tstart=datetime.now()
      my_board.setLow(ledPin)
      offed=1
  time.sleep(1)
  j+=1 
tstat = tend-tstart
print tstat.microseconds

tstart = datetime.now()
time.sleep(3)
tend = datetime.now()
tstat = tend-tstart
print tstat.microseconds
my_board.close()
