# Servomotor Control

A web-based interface for controlling a servomotor connected to an Arduino using a Flask application.

## Description

Servomotor Control is a simple web application that allows users to control the angle of a servomotor attached to an Arduino. The system uses a Flask backend to create a user-friendly interface where users can input the desired angle (0-180 degrees) and send it to the servomotor. The clean, responsive Bootstrap-based interface makes it easy to use on both desktop and mobile devices.

## Getting Started

### Dependencies

* Python 3.6 or higher
* Flask
* pyserial
* Arduino IDE
* Bootstrap 5 (included via CDN)
* Arduino board (Any model with USB connectivity should work)
* Servomotor
* PC or Raspberry Pi to run the Flask server

### Hardware Setup

1. Connect your servomotor to the Arduino:
   * Connect the servo power wire (usually red) to 5V on the Arduino
   * Connect the servo ground wire (usually black or brown) to GND on the Arduino
   * Connect the servo signal wire (usually yellow, orange, or white) to pin 9 on the Arduino

2. Connect the Arduino to your computer via USB

### Software Setup

1. Install the required Python packages:
```
pip install flask pyserial
```

2. Upload the Arduino code to your board using the Arduino IDE

3. Find your Arduino's serial port name:
   * Windows: It will appear as 'COM3', 'COM4', etc. in Device Manager
   * Linux: Usually '/dev/ttyACM0' or '/dev/ttyUSB0'
   * Mac: Usually '/dev/tty.usbmodem*' or '/dev/tty.usbserial*'

4. Update the `SERIAL_PORT` variable in the Flask application code to match your Arduino's port.

### Executing Program

1. Run the Flask application:
```
python app.py
```

2. Open a web browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Use the web interface to input the desired angle (0-180 degrees) and click "Enviar" to send the command to the servomotor.

## Common Issues

* **Serial Port Connection Errors**: Ensure you've specified the correct serial port in the Flask application.
* **Servomotor Not Moving**: Check your wiring connections and ensure the servo is receiving proper power.
* **Values Outside Range**: The application restricts input to 0-180 degrees, which is the standard range for most servomotors.

## Acknowledgments

* Thanks to my Professor JBMichin for your never-ending charisma
