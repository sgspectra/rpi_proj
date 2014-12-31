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
    time.sleep(0.5)
    GPIO.output(red,GPIO.LOW)
    
def sht():
    GPIO.output(red,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(red,GPIO.LOW)
    
def morseCode(x):
    if x == 'a' or 'A':
        sht()
        lng()
    elif x == 'b' or 'B':
        lng()
        sht()
        sht()
        sht()
    elif x == 'c' or 'C':
        lng()
        sht()
        lng()
        sht()
    elif x == 'd' or 'D':
        lng()
        sht()
        sht()
    elif x == 'e' or 'E':
        sht()
    elif x == 'f' or 'F':
        sht()
        sht()
        lng()
        sht()
    elif x == 'g' or 'G':
        lng()
        lng()
        sht()
    elif x == 'h' or 'H':
        sht()
        sht()
        sht()
        sht()
    elif x == 'i' or 'I':
        sht()
        sht()
    elif x == 'j' or 'J':
        sht()
        lng()
        lng()
        lng()
    elif x == 'k' or 'K':
        lng()
        sht()
        lng()
    elif x == 'l' or 'L':
        sht()
        lng()
        sht()
        sht()
    elif x == 'm' or 'M':
        lng()
        lng()
    elif x == 'n' or 'N':
        lng()
        sht()
    elif x == 'o' or 'O':
        lng()
        lng()
        lng()
    elif x == 'p' or 'P':
        sht()
        lng()
        lng()
        sht()
    elif x == 'q' or 'Q':
        lng()
        lng()
        sht()
        lng()
    elif x == 'r' or 'R':
        sht()
        lng()
        sht()
    elif x == 's' or 'S':
        sht()
        sht()
        sht()
    elif x == 't' or 'T':
        lng()
    elif x == 'u' or 'U':
        sht()
        sht()
        lng()
    elif x == 'v' or 'V':
        sht()
        sht()
        sht()
        lng()
    elif x == 'w' or 'W':
        sht()
        lng()
        lng()
    elif x == 'x' or 'X':
        lng()
        sht()
        sht()
        lng()
    elif x == 'y' or 'Y':
        lng()
        sht()
        lng()
        lng()
    elif x == 'z' or 'Z':
        lng()
        lng()
        sht()
        sht()        

str1 = input('Please enter string to translate to morse code: ')

for c in str1:
    morseCode(c)                                                                               