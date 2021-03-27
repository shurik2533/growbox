import RPi.GPIO as GPIO
import time

CHANNEL = 7
CHANNEL2 = 8
CHANNEL3 = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)
GPIO.setup(CHANNEL2, GPIO.OUT)
GPIO.setup(CHANNEL3, GPIO.OUT)

T = 3

try:
    GPIO.output(CHANNEL, GPIO.HIGH)
    GPIO.output(CHANNEL2, GPIO.HIGH)
    GPIO.output(CHANNEL3, GPIO.HIGH)
    time.sleep(4)

finally:
    GPIO.output(CHANNEL, GPIO.LOW)
    GPIO.output(CHANNEL2, GPIO.LOW)
    GPIO.output(CHANNEL3, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()