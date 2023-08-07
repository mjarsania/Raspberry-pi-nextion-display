import serial
import time

# Replace the serial port name with the correct port for your Nextion display
serial_port = '/dev/ttyUSB0'

# Set the baud rate to match the Nextion display (default is 9600)
baud_rate = 9600

# Create a serial connection to the Nextion display
ser = serial.Serial(serial_port, baud_rate, timeout=5)

while True:
    try:
        # Read data from the Nextion display
        #data = ser.readline().decode().strip()
        data = ser.readline()

        if data:
            print("Received: ", data) 

    except KeyboardInterrupt:
        print("Exiting...")
        break

# Close the serial connection
ser.close()
