#James Dutton Discussion7

import RPi.GPIO as GPIO
import time

led_pin = 17
switch1 = 27
switch2 = 22
BRIGHTNESS = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(BRIGHTNESS)
while True:
    if GPIO.input(switch1) == False:       
        print("Increment Pressed")
        if BRIGHTNESS < 100:
            BRIGHTNESS+=5
        pwm_led.ChangeDutyCycle(BRIGHTNESS)
        time.sleep(0.5)
    if GPIO.input(switch2) == False:
        print("Decrement Pressed")
        if BRIGHTNESS > 5:
            BRIGHTNESS-=5
        pwm_led.ChangeDutyCycle(BRIGHTNESS)
        time.sleep(0.5)
#pwm_led.ChangeDutyCycle(50)
#try:
 #   while True:
  #      duty_s = raw_input("Enter the brightness percentage: ")
   #     duty = int(duty_s)
    #    pwm_led.ChangeDutyCycle(duty)
#finally:
 #   print("Cleaing up")
  #  GPIO.cleanup()
