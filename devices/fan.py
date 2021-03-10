import RPi.GPIO as GPIO


class Fan:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 1000)
        self.speed = 100
        self.pwm.start(self.speed)

    def set_speed(self, speed):
        self.speed = speed
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm.stop()
