#James Dutton
#ECE492/ME492
#Homework 1
#June 2 2017

import RPi.GPIO as GPIO#Imports needed to use the pins
GPIO.setmode(GPIO.BCM)

pins = [17,18,27]#set the pins that will go to the LEDs
INPUT = 0 #variable to keep track of user choice
#initializing pins
for i, pin in enumerate(pins):
        GPIO.setup(pin, GPIO.OUT)
#while loop so user can continuously "play the game"
while(INPUT != '4'):
#get the input that is necesarry to run the program
        INPUT = raw_input("Enter 1 for 1 LED 2 for 2 LEDs 3 for 3 LEDs or 4 to quit ")
#Create effectively a switch statement that checks to see what the input is input is a string even when an int is entered so I just check against chars.
        if INPUT == '1':
                GPIO.output(17,1)
                GPIO.output(18,0)
                GPIO.output(27,0)
        elif INPUT == '2':
                GPIO.output(17,1)
                GPIO.output(18,1)
                GPIO.output(27,0)
        elif INPUT == '3':
                GPIO.output(17,1)
                GPIO.output(18,1)
                GPIO.output(27,1)
        else:
                if INPUT != '4':
                        print('Sorry that was not an option, please try again')
                #turn off all LEDs and cleanup GPIO
                GPIO.output(17,0)
                GPIO.output(18,0)
                GPIO.output(27,0)
print('Thank you for participating, closing program normally.')#let user know the program exited correctly
GPIO.cleanup()


                
