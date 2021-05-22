import RPi.GPIO as GPIO

from logger import get_logger

FAN_TOP_PIN = 17
FAN_BOTTOM_PIN = 27

MAX_SPEED = 100

LOGGER = get_logger()

class Fan:
    def __init__(self, pin, min_speed):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 1000)
        self.pwm.start(MAX_SPEED)
        self.min_speed = min_speed

    def __exit__(self):
        LOGGER.info('exit!!!!!!!!!!!!!')
        self.pwm.stop()

    def set_speed(self, speed):
        self.pwm.ChangeDutyCycle(speed)
