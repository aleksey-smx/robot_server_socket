import RPi.GPIO as GPIO
import socket
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

GPIO.output(29, True)
GPIO.output(31, True)

UDP_IP = "0.0.0.0"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
		raw=sock.recvfrom(1024)

		#print type(raw)
		rawnew = ('forward', 'stop', 'backward', 'left', 'right' )

		print type(rawnew)

		if raw[0] == rawnew[0]:
			print 'robot moves forward'
			GPIO.output(33, True)
			GPIO.output(11, False)
			GPIO.output(13, True)
			GPIO.output(15, False)
			time.sleep(1)

		elif raw[0] == rawnew[1]:
			print 'robot stop'
			GPIO.output(33, False)
			GPIO.output(11, False)
			GPIO.output(13, False)
			GPIO.output(15, False)
			time.sleep(1)

		elif raw[0] == rawnew[2]:
			print "robot moves backward"
			GPIO.output(33, False)
			GPIO.output(11, True)
			GPIO.output(13, False)
			GPIO.output(15, True)
			time.sleep(1)

		elif raw[0] == rawnew[3]:
			print "robot moves left"
			GPIO.output(33, False)
			GPIO.output(11, True)
			GPIO.output(13, True)
			GPIO.output(15, False)
			time.sleep(1)

		elif raw[0] == rawnew[4]:
			print "robot moves right"
			GPIO.output(33, True)
			GPIO.output(11, False)
			GPIO.output(13, False)
			GPIO.output(15, True)
			time.sleep(1)
		else:
			print "message error"
			GPIO.output(33, False)
			GPIO.output(11, False)
			GPIO.output(13, False)
			GPIO.output(15, False)
			time.sleep(1)
