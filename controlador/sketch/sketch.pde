const int sensorPin = A0;    // pin that the sensor is attached to
const int sensorPin2 = A1;
const int ledPin = 9;        // pin that the LED is attached to

// variables:
int sensorValue = 0;         // the sensor value
int sensorValue2 = 0;
int sensorMin = 1023;        // minimum sensor value
int sensorMin2 = 1023;
int sensorMax = 0;           // maximum sensor value
int sensorMax2 = 0;

int opcion = 0;
int t_inicio, t_fin, t_diferencia;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(13, HIGH);
  while (millis() < 5000) {
    sensorValue = analogRead(sensorPin);
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }
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
    comando();
    if(Serial.available()>0){
	opcion = int(Serial.read()) - 48;
	if(opcion==1){
	    sensorValue=analogRead(sensorPin);
	    while(sensorValue!=0){
		sensorValue=analogRead(sensorPin);
		sensorValue=map(sensorValue,sensorMin,sensorMax,0,255);
		sensorValue=constrain(sensorValue,0,255);
		t_inicio=millis();
		digitalWrite(ledPin, HIGH);
	    }
	    sensorValue=analogRead(sensorPin2);
	    while(sensorValue=!0){
		sensorValue=analogRead(sensorPin2);
		sensorValue=map(sensorValue,sensorMin2,sensorMax2,0,255);
		sensorValue=constrain(sensorValue,0,255);
		t_fin=millis();
		digitalWrite(ledPin,LOW);
	    }
	    t_diferencia = t_fin - t_inicio;
	    Serial.println(t_diferencia);
	}
   }
}
void datos(){
    Serial.println("Que");
}

void comando(){
    datos();
    while(Serial.available()<=0){}
}
