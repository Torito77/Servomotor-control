#include <Servo.h>

Servo myservo;  
int servoPin = 9;

// string to hold incoming data
String inputString = "";
// whether the string is complete
boolean string_complete = false; 

void setup() {
  Serial.begin(9600); // initialize serial communication
  myservo.attach(servoPin); // attaches the servo
  inputString.reserve(10); // reserve space for the string
}

void loop() {
  if (string_complete) {
    int angle = inputString.toInt(); // convert string to integer
    
    // validate the angle (0-180)
    if (angle >= 0 && angle <= 180) {
      myservo.write(angle); 
    }
    
    // Reset variables
    inputString = "";
    string_complete = false;
  }
}

// SerialEvent occurs whenever new data comes in
void serialEvent() {
  while (Serial.available()) {
    char input_char = (char)Serial.read(); // get the new byte
    if (input_char == '\n') {
      string_complete = true;
    } else {
      // add it to the inputString if it's not a newline
      inputString += input_char;
    }
  }
}
