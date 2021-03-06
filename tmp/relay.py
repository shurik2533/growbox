import RPi.GPIO as GPIO
import time

CHANNEL = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)


#try:
GPIO.output(CHANNEL, GPIO.HIGH)
time.sleep(2)
GPIO.output(CHANNEL, GPIO.LOW)
GPIO.cleanup()
#finally:
#    GPIO.cleanup()
