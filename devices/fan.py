import RPi.GPIO as GPIO

FAN_TOP_PIN = 17
FAN_BOTTOM_PIN = 27

MAX_SPEED = 100


class Fan:
    def __init__(self, pin, min_speed):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 1000)
        self.pwm.start(MAX_SPEED)
        self.min_speed = min_speed

    def stop(self):
        self.pwm.stop()

    def set_speed(self, speed):
        self.pwm.ChangeDutyCycle(speed)
