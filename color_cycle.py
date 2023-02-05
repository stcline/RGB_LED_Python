#libraries
import RPi.GPIO as GPIO
from time import sleep

#disable warnings (optional)
GPIO.setwarnings(False)

#Select GPIO Mode
GPIO.setmode(GPIO.BCM)

#Set pins
redPin = 17
greenPin = 27
bluePin = 22

#Set pins as output
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

red = GPIO.PWM(redPin, 75)
green = GPIO.PWM(greenPin, 75)
blue = GPIO.PWM(bluePin, 75)

def setColor ():

	red_val = int(input("What duty cycle for the red LED?"))
	green_val = int(input("What duty cycle for the green LED?"))
	blue_val = int(input("What duty cycle for the blue LED?"))

	red.start(red_val/2.55)
	green.start(green_val/2.55)
	blue.start(blue_val/2.55)

	sleep (3)

	red.start(0)
	green.start(0)
	blue.start(0)

while True:
        setColor()
