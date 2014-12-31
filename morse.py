import RPi.GPIO as GPIO
import time

#set up GPIO infomation
red = 11
green = 37

chan_list = [red,green]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(chan_list,GPIO.OUT)

def lng():
    GPIO.output(red,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(red,GPIO.LOW)
    time.sleep(0.1)

def sht():
    GPIO.output(red,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(red,GPIO.LOW)
    time.sleep(0.1)
	    
def morseCode(x):
    if x == 'a' or x == 'A':
        sht()
        lng()
    elif x == 'b' or x == 'B':
        lng()
        sht()
        sht()
        sht()
    elif x == 'c' or x == 'C':
        lng()
        sht()
        lng()
        sht()
    elif x == 'd' or x == 'D':
        lng()
        sht()
        sht()
    elif x == 'e' or x == 'E':
        sht()
    elif x == 'f' or x == 'F':
        sht()
        sht()
        lng()
        sht()
    elif x == 'g' or x == 'G':
        lng()
        lng()
        sht()
    elif x == 'h' or x == 'H':
        sht()
        sht()
        sht()
        sht()
    elif x == 'i' or x == 'I':
        sht()
        sht()
    elif x == 'j' or x == 'J':
        sht()
        lng()
        lng()
        lng()
    elif x == 'k' or x == 'K':
        lng()
        sht()
        lng()
    elif x == 'l' or x == 'L':
        sht()
        lng()
        sht()
        sht()
    elif x == 'm' or x == 'M':
        lng()
        lng()
    elif x == 'n' or x == 'N':
        lng()
        sht()
    elif x == 'o' or x == 'O':
        lng()
        lng()
        lng()
    elif x == 'p' or x == 'P':
        sht()
        lng()
        lng()
        sht()
    elif x == 'q' or x == 'Q':
        lng()
        lng()
        sht()
        lng()
    elif x == 'r' or x == 'R':
        sht()
        lng()
        sht()
    elif x == 's' or x == 'S':
        sht()
        sht()
        sht()
    elif x == 't' or x == 'T':
        lng()
    elif x == 'u' or x == 'U':
        sht()
        sht()
        lng()
    elif x == 'v' or x == 'V':
        sht()
        sht()
        sht()
        lng()
    elif x == 'w' or x == 'W':
        sht()
        lng()
        lng()
    elif x == 'x' or x == 'X':
        lng()
        sht()
        sht()
        lng()
    elif x == 'y' or x == 'Y':
        lng()
        sht()
        lng()
        lng()
    elif x == 'z' or x == 'Z':
        lng()
        lng()
        sht()
        sht()        
    elif x == ' ':
	time.sleep(0.7)

str1 = raw_input('Please enter string to translate to morse code: ')

for i in range(0, len(str1)):
    morseCode(str1[i])                                                                               
