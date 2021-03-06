import RPi.GPIO as GPIO
import time


CHANNEL1 = 8
CHANNEL2 = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL1, GPIO.IN)
GPIO.setup(CHANNEL2, GPIO.IN)

def get_wet(val):
    return 'dry' if val else 'wet'


try:
    while True:
        print('Sensor1: ' + get_wet(GPIO.input(CHANNEL1)))
        print('Sensor2: ' + get_wet(GPIO.input(CHANNEL2)))
        print('----------------------------')
        time.sleep(1)
finally:
    GPIO.cleanup()
