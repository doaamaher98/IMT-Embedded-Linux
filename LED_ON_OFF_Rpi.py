############################################################
###   Author      : Doaa Maher                  		####
###   File 		  : Turning LED ON/OFF ON Raspberry Pi	####
###   Date        : 18 JAN 2021                  		####
###   Version     : 1.0                         		####
############################################################
import RPi.GPIO as GPIO

#First step is setting up the numbering system [BOARD or BCM] Modes
GPIO.setmode(GPIO.BCM)

#Second Setting up the INPUT and OUTPUT PINS on Raspberry
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

try:
#Third Setting up the Values
    while True :
        Value = str(input("Please enter the mode of the LED : "))
        if Value == 'ON' :
            GPIO.output(2,GPIO.HIGH)
            GPIO.output(3,GPIO.HIGH)
        elif Value == 'OFF' :
            GPIO.output(2,GPIO.LOW)
            GPIO.output(3,GPIO.LOW)
        else :
            print("Invalid Syntax, Try again!")
except KeyboardInterrupt :
    GPIO.cleanup()
