############################################################
###   Author      : Doaa Maher                  		####
###   File 		  : Push Button					        ####
###   Date        : 18 JAN 2021                  		####
###   Version     : 1.0                         		####
############################################################
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT) 
GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP) 

while True:
	PinValue=GPIO.input(3)
	time.sleep(0.1) # For debouncing time (100msec)
	if PinValue==0:
		GPIO.output(2,GPIO.HIGH)
	else:
		GPIO.output(2,GPIO.LOW)
