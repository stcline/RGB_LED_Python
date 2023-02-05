#This script uses the RGB module to control an RGB LED from user input

from RGB import RGB

#Set the board to GPIO BCM
RGB.boardSetup()
#Create an RGB object
rgb = RGB(17,27,22)
#Turn on the rgb
rgb.colorOn(255,0,0,3)
