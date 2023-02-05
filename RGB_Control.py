#This script uses the RGB module to control an RGB LED from user input

from RGB import RGB

#Set the board to GPIO BCM
RGB.boardSetup()
#Create an RGB object
rgb = RGB(17,27,22)

rval = int(input(" What duty cycle would you like to use for red? "))
gval = int(input(" What duty cycle would you like to use for green? "))
bval = int(input(" Whad duty cycle would you like to use for blue? "))
dur = int(input(" How long would you like it to stay on? "))

print()
print(" Here is your custom color...")
print()

#Turn on the rgb
rgb.colorOn(rval,gval,bval,dur)
