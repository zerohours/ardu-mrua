#include <Servo.h> 

//Defining Variables

//Dedicated Arduino Pins

const int pin_first_photocell = A0; 
const int pin_second_photocell = A1;
const int pin_servo = 9;
const int pin_led = 13; 

// Other Damn variables
int sensor_value = 0;
int sensor_min = 1023;
int sensor_min2 = 1023;
int sensor_max = 0;
int sensor_max2 = 0;

Servo myservo;
int servo_position = 0;
int option = 0;
int t_start, t_end, t_diff;

void setup() {
  Serial.begin(9600);
  myservo.attach(pin_servo);
  pinMode(pin_led, OUTPUT);
  digitalWrite(pin_led, HIGH);
  while (millis() < 5000) {
    sensor_value = analogRead(pin_first_photocell);
    if (sensor_value > sensor_max) {
      sensor_max = sensor_value;
    }
    if (sensor_value < sensor_min) {
      sensor_min = sensor_value;
    }
  }
  sensor_value = 0;
  while (millis() < 10000) {
    sensor_value = analogRead(pin_second_photocell);
    if (sensor_value > sensor_max2) {
      sensor_max2 = sensor_value;
    }
    if (sensor_value < sensor_min2) {
      sensor_min2 = sensor_value;
    }
  }
  digitalWrite(pin_led, LOW);
}

void loop() {
    command();
    if(Serial.available()>0){
	option = int(Serial.read()) - 48;
	if(option==1){
	    sensor_value=analogRead(pin_first_photocell);
	    while(sensor_value>=10){
		sensor_value=analogRead(pin_first_photocell);
		sensor_value=map(sensor_value,sensor_min,sensor_max,0,255);
		sensor_value=constrain(sensor_value,0,255);
                Serial.println(sensor_value);
		t_start=millis();
		digitalWrite(pin_led, HIGH);
	    }
	    sensor_value=analogRead(pin_second_photocell);
	    while(sensor_value>=10){
		sensor_value=analogRead(pin_second_photocell);
		sensor_value=map(sensor_value,sensor_min2,sensor_max2,0,255);
		sensor_value=constrain(sensor_value,0,255);
                Serial.println(sensor_value);
		t_end=millis();
		digitalWrite(pin_led,LOW);
	    }
	    t_diff = t_end - t_start;
	    Serial.println(t_diff);
	}
        if(option==2){
	    	command();
		servo_position = Serial.read();
                Serial.print("Posicion buscada: ");
                Serial.println(servo_position);
		int servo_current = myservo.read();
                Serial.print("Posicion actual: ");
                Serial.println(servo_current);
		if ( servo_position > servo_current ) {
		    	int step;
			for (step = servo_current;step<servo_position;step += 1){
                            Serial.println(step);
			    myservo.write(step);
			    delay(15);
			}
		} else {
		    int step;
		    for (step = servo_current;step>servo_position; step -= 1){
                        Serial.println(step);
			myservo.write(step);
			delay(15);
		    }
		}

	}
   }
}
void ask_data(){
    Serial.println("wtf");
}

void command(){
    ask_data();
    while(Serial.available()<=0){}
}

void moverServo(){
  for(servo_position = 0; servo_position < 180; servo_position += 1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(servo_position);              // tell servo to go to servo_position in variable 'servo_position' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  for(servo_position = 180; servo_position>=1; servo_position-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(servo_position);              // tell servo to go to position in variable 'servo_position' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  }
}
