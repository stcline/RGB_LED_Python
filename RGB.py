#This module may be used to set up the RGB objects for use with 
# these methods.

#Import required modules
from time import sleep
import RPi.GPIO as GPIO

def boardSetup():
  #disable warnings
  GPIO.setwarnings(False)
  #Select GPIO Mode
  GPIO.setmode(GPIO.BCM)

#Create a class to control the RGB LED
class RGB:
  def __init__(self, red_pin, green_pin, blue_pin):
    #set red,green and blue pins
    self.redPin = red_pin
    self.greenPin = green_pin
    self.bluePin = blue_pin
    #set pins as outputs
    GPIO.setup(self.redPin,GPIO.OUT)
    GPIO.setup(self.greenPin,GPIO.OUT)
    GPIO.setup(self.bluePin,GPIO.OUT)

  def colorOn(self, red_val, green_val, blue_val, duration):
    #create objects for pins
    red = GPIO.PWM(self.redPin, 75)
    green = GPIO.PWM(self.greenPin, 75)
    blue = GPIO.PWM(self.bluePin, 75)

    red.start(red_val/2.55)
    green.start(green_val/2.55)
    blue.start(blue_val/2.55)
    sleep(duration)
    red.start(0)
    green.start(0)
    blue.start(0)

#Set the board to GPIO BCM
#boardSetup()
#Create an RGB object
#rgb = RGB(17,27,22)
#Turn on the rgb
#rgb.colorOn(255,0,0,3)
