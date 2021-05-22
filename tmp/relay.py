import RPi.GPIO as GPIO 
import time

CHANNEL = 7
CHANNEL2 = 8
CHANNEL3 = 25
CHANNEL4 = 9
CHANNEL5 = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)
GPIO.setup(CHANNEL2, GPIO.OUT)
GPIO.setup(CHANNEL3, GPIO.OUT)
GPIO.setup(CHANNEL4, GPIO.OUT)
GPIO.setup(CHANNEL5, GPIO.OUT)

T = 2

#GPIO.output(CHANNEL2, GPIO.HIGH)
#GPIO.output(CHANNEL3, GPIO.HIGH)

try:
    while True:
#        GPIO.output(CHANNEL2, GPIO.LOW)
#        GPIO.output(CHANNEL3, GPIO.LOW)

        time.sleep(T)
#        GPIO.output(CHANNEL, GPIO.HIGH)
#        time.sleep(T)
    
#        GPIO.output(CHANNEL2, GPIO.LOW)
#        time.sleep(T)
#        GPIO.output(CHANNEL2, GPIO.HIGH)
    
#        GPIO.output(CHANNEL3, GPIO.LOW)
#        time.sleep(T)
#        GPIO.output(CHANNEL3, GPIO.HIGH)
#        time.sleep(1)

        GPIO.output(CHANNEL, GPIO.LOW)    
        GPIO.output(CHANNEL2, GPIO.LOW)
        GPIO.output(CHANNEL3, GPIO.LOW)
        GPIO.output(CHANNEL4, GPIO.LOW)
        GPIO.output(CHANNEL5, GPIO.LOW) 
        time.sleep(T)
        GPIO.output(CHANNEL, GPIO.HIGH)
        GPIO.output(CHANNEL2, GPIO.HIGH)
        GPIO.output(CHANNEL3, GPIO.HIGH)
        GPIO.output(CHANNEL4, GPIO.HIGH)
        GPIO.output(CHANNEL5, GPIO.HIGH)
finally:
#    GPIO.output(CHANNEL, GPIO.HIGH)
#    GPIO.output(CHANNEL2, GPIO.HIGH)
#    GPIO.output(CHANNEL3, GPIO.HIGH)
    GPIO.cleanup()
