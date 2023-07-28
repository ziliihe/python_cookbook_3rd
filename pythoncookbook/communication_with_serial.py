import serial
import datetime

ser = serial.Serial('/dev/tty2', baudrate=9600, bytesize=8, parity='N', stopbits=1)
message = f"hello world, {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
ser.write(message.encode())
