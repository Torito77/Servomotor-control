import serial, time
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5


#Flask initialization code
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cRUz-4Zu1-CAmPe0n-2030'
Bootstrap5(app)


SERIAL_PORT = 'COM3'  
BAUD_RATE = 9600
def send_to_arduino(angle):
    try:
        # Open the serial connection
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the Arduino to initialize
        
        # Send the angle value followed by a newline
        ser.write(f"{angle}\n".encode())
        time.sleep(0.1)  # Give Arduino time to process
        
        # Close the connection
        ser.close()
        return True
    
    except Exception as e:
        print(f"Error communicating with Arduino: {e}")
        return False


# Endpoints - - - - - - - - - - - - - - - - - - - - - - - - >
@app.route('/', methods=["GET","POST"])
def home():
    angle = 90
    
    if request.method == 'POST':
        
        angle = request.form.get('angle', type=int)
        send_to_arduino(angle)
        
        if angle is not None and (0 <= angle <= 180):
            if send_to_arduino(angle):
                message = f"Successfully sent angle: {angle}°"
            else:
                message = "Failed to communicate with Arduino"
        else:
            message = "Invalid angle value. Must be between 0 and 180."
    
    return render_template('index.html',degrees=angle, message=message)


if __name__ == "__main__":
    app.run(debug=True)