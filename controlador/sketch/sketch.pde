const int sensorPin = 0;    // pin that the sensor is attached to
const int sensorPin2 = 1;
const int ledPin = 9;        // pin that the LED is attached to

// variables:
int sensorValue = 0;         // the sensor value
int sensorValue2 = 0;
int sensorMin = 1023;        // minimum sensor value
int sensorMin2 = 1023;
int sensorMax = 0;           // maximum sensor value
int sensorMax2 = 0;

void setup() {
  // turn on LED to signal the start of the calibration period:
  pinMode(13, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(13, HIGH);
  Serial.begin(9600);
  // calibrate during the first five seconds 
  while (millis() < 5000) {
    sensorValue = analogRead(sensorPin);
    // record the maximum sensor value
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }
    // record the minimum sensor value
    if (sensorValue < sensorMin) {
      sensorMin = sensorValue;
    }
  }
  while (millis() < 10000) {
    sensorValue = analogRead(sensorPin2);
    if (sensorValue > sensorMax2) {
      sensorMax = sensorValue;
    }
    if (sensorValue < sensorMin2) {
      sensorMin2 = sensorValue;
    }
  } 
  digitalWrite(13, LOW);
}

void loop() {
  // read first sensor
  sensorValue=analogRead(sensorPin);
  // apply the calibration to the sensor reading
  sensorValue=map(sensorValue,sensorMin,sensorMax,0,255);
  // in case the sensor value is outside the range seen during calibration
  sensorValue=constrain(sensorValue,0,255);
  int tstart, tend, tdiff;
  if(sensorValue==0){
    Serial.print("Iniciando con: ");
    digitalWrite(ledPin, HIGH);
    tstart=millis();
    Serial.println(tstart);
    sensorValue=analogRead(sensorPin2);
    sensorValue=map(sensorValue,sensorMin,sensorMax,0,255);
    sensorValue=constrain(sensorValue,0,255);
    while(sensorValue!=0){
      sensorValue=analogRead(sensorPin2);
      sensorValue=map(sensorValue,sensorMin,sensorMax,0,255);
      sensorValue=constrain(sensorValue,0,255);
      if(sensorValue==0){
        tend=millis();
        digitalWrite(ledPin,LOW);
        Serial.print("Terminando con: ");
        Serial.println(tend);
      }
    }
    tdiff=tend-tstart;
    Serial.print("El tiempo es:");
    Serial.println(tdiff);
    Serial.println("esperando...");
    delay(10000);
  }
}
