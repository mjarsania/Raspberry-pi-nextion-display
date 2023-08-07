import serial
import time
import struct

def send_command(ser, command):
    end_cmd = b'\xFF\xFF\xFF'
    full_cmd = command.encode() + end_cmd
    ser.write(full_cmd)

try:
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    time.sleep(1)  # Allow time for the Nextion display to initialize after the serial connection is opened

    command = 't0.txt="Nextion"'
    send_command(ser, command)

    # You can add more commands here to control other components on the Nextion display if needed.

except serial.SerialException as e:
    print("Serial Port Error: ", e)

except Exception as e:
    print("Error: ", e)

finally:
    if ser.is_open:
        ser.close()
