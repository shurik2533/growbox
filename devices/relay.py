import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

LIGHT_1 = 8
LIGHT_2 = 25
HEAT = 7
PUMP_TOP = 9
PUMP_BOTTOM = 11

CHANNELS = [LIGHT_1, LIGHT_2, HEAT, PUMP_TOP, PUMP_BOTTOM]
[GPIO.setup(channel, GPIO.OUT) for channel in CHANNELS]
[GPIO.output(channel, GPIO.HIGH) for channel in CHANNELS]


def on(pin):
    GPIO.output(pin, GPIO.LOW)


def off(pin):
    GPIO.output(pin, GPIO.HIGH)
