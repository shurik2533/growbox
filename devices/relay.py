import RPi.GPIO as GPIO


LIGHT_1 = 8
LIGHT_2 = 25
HEAT = 7
PUMP_1 = 9
PUMP_2 = 11

CHANNELS = [LIGHT_1, LIGHT_2, HEAT, PUMP_1, PUMP_2]
[GPIO.setup(channel, GPIO.OUT) for channel in CHANNELS]
[GPIO.output(channel, GPIO.HIGH) for channel in CHANNELS]


def on(pin):
    GPIO.output(pin, GPIO.LOW)


def off(pin):
    GPIO.output(pin, GPIO.HIGH)
