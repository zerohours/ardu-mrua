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
            Serial.println(sensor_value);
	    while(sensor_value>=10){
		sensor_value=analogRead(pin_first_photocell);
		sensor_value=map(sensor_value,sensor_min,sensor_max,0,255);
		sensor_value=constrain(sensor_value,0,255);
                Serial.println(sensor_value);
		t_start=millis();
		digitalWrite(pin_led, HIGH);
	    }
	    sensor_value=analogRead(pin_second_photocell);
            Serial.println(sensor_value);
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
            delay(10000);
	}
        if(option==2){
	    	ask_data();
		servo_position = int(Serial.read()) - 48;
                if(servo_position == 0) {myservo.write(95); }
                if(servo_position == 1) {myservo.write(105); }
                if(servo_position == 2) {myservo.write(120); }
                if(servo_position == 3) {myservo.write(135); }
                if(servo_position == 4) {myservo.write(150); }
                if(servo_position == 5) {myservo.write(165); }
                if(servo_position == 6) {myservo.write(180); }
                if(servo_position == 16) {myservo.write(15);}
                if(servo_position == 25) {myservo.write(30);}
                if(servo_position == 34) {myservo.write(45);}
                if(servo_position == 43) {myservo.write(60);}
                if(servo_position == 52) {myservo.write(75);}
                if(servo_position == 61) {myservo.write(90);}
                if(servo_position == 0) {myservo.write(5);}
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
