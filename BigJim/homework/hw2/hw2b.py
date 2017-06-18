#James Dutton hw2b Cylon
import RPi.GPIO as GPIO #import to use the pins
import time
GPIO.setmode(GPIO.BCM)
pin_a = 4
pin_b = 17
pin_c = 18
pin_d = 27
counter = 0 #determine what state we are in
#turn on LEDs to be output
GPIO.setup(pin_a, GPIO.OUT)
GPIO.setup(pin_b, GPIO.OUT)
GPIO.setup(pin_c, GPIO.OUT)
GPIO.setup(pin_d, GPIO.OUT)
while counter < 50:#arbitrary number of times for the progeram to run
    #state 1 (Each state corresponds to an increment of the counter
    #I just use modulo and if statements for a quick naive solution
    #to this problem
    if counter % 8 == 0:
        GPIO.output(pin_a,1)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,0)
    #state 2
    if counter % 8 == 1:
        GPIO.output(pin_a,0)        
        GPIO.output(pin_b,1)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,0)
    #state 3
    if counter % 8 == 2:
        GPIO.output(pin_a,0)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,1)
        GPIO.output(pin_d,0)
    #state 4
    if counter % 8 == 3:
        GPIO.output(pin_a,0)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,1)
    #state 5
    if counter % 8 == 4:
        GPIO.output(pin_a,0)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,1)
    #state 6
    if counter % 8 == 5:
        GPIO.output(pin_a,0)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,1)
        GPIO.output(pin_d,0)
    #state 7
    if counter % 8 == 6:
        GPIO.output(pin_a,0)
        GPIO.output(pin_b,1)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,0)
    #state 8
    if counter % 8 == 7:
        GPIO.output(pin_a,1)
        GPIO.output(pin_b,0)
        GPIO.output(pin_c,0)
        GPIO.output(pin_d,0)
    counter+=1
    time.sleep(.5)

#turn off LEDs and cleanup GPIO    
GPIO.output(pin_a,0)
GPIO.output(pin_b,0)
GPIO.output(pin_c,0)
GPIO.output(pin_d,0)
GPIO.cleanup()

