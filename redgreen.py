import RPi.GPIO as GPIO
import time

red = 11
green = 37

chan_list = [red,green]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(chan_list,GPIO.OUT)

x = 0

while(x<5):
	GPIO.output(red,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(green,GPIO.LOW)
	x += 1
